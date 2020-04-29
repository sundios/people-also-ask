#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 00:07:02 2020

@author: konradburchardt
"""

from selenium.common.exceptions import NoSuchElementException    
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import xlsxwriter
import datetime
import time
import os

def returnChromeDriver(pathToChromeDriver):
	chrome_options = Options()
	chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 1, 'profile.managed_default_content_settings.images': 1, 'profile.managed_default_content_settings.stylesheet': 2} )
	chromedriver = pathToChromeDriver
	userAgent = "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver, chrome_options = chrome_options)
	return driver

def returnSearchUrl(question):
	baseGoogleQuery = "https://www.google.com/search?q="
	searchUrl = baseGoogleQuery + question.lower().replace(" ", "+").replace("?", "%3F").replace("'", "%27")
	return searchUrl

def clickQuestions(driver, question, totalClicks):
	searchUrl = returnSearchUrl(question)
	driver.get(searchUrl)
	time.sleep(1)

	if driver.find_elements_by_css_selector('div.related-question-pair'):
		questionIndex = 0
		questions = driver.find_elements_by_css_selector('div.related-question-pair')
		questions[-1].location_once_scrolled_into_view

		while(questionIndex < totalClicks):
			questions[questionIndex].click()
			time.sleep(1)
			questions = driver.find_elements_by_css_selector('div.related-question-pair')
			questions[questionIndex + 1].location_once_scrolled_into_view
			questionIndex = questionIndex + 1

	return driver

def extractQuestionData(soup):
	questionList = []
	for question in soup.findAll("div", class_="related-question-pair"):
		questionDict = {}
		questionDict['relatedQuestion'] = question.find("g-accordion-expander").find("div").text

		if question.find("h3"):
			questionDict['titleTag'] = question.find("h3").text
			questionDict['titleTagLength'] = len(questionDict['titleTag'])
		else:
			questionDict['titleTag'] = "N/A - ERROR?"
			questionDict['titleTagLength'] = "N/A - ERROR?"

		if question.find("div", {"role":"heading"}):
			questionDict['answer'] = question.find("div", {"role":"heading"}).text
			questionDict['answerLength'] = len(questionDict['answer'])
		else:
			try:
				questionDict['answer'] = question.find("g-accordion-expander").findAll("div")[2].text
				questionDict['answerLength'] = len(questionDict['answer'])
			except:
				questionDict['answer'] = "N/A"
				questionDict['answerLength'] = "N/A"					

		if question.find("div", class_="r"):
			questionDict['questionUrl'] = question.find("div", class_="r").find("a")['href']
		else:
			questionDict['questionUrl'] = "N/A - ERROR"

		questionList.append(questionDict)

	return questionList

def writeExcelFile(allExtractedDataList):
	date = datetime.datetime.now()
	workbook = xlsxwriter.Workbook("data-" + date.strftime("%b-%d-%Y-%H-%M-%S") + ".xlsx", {'strings_to_urls': True})
	worksheet01 = workbook.add_worksheet("Data")
	worksheet01.write(0, 0, "Initial Question")
	worksheet01.write(0, 1, "Related Question")
	worksheet01.write(0, 2, "Title Tag")
	worksheet01.write(0, 3, "Title Tag Length")
	worksheet01.write(0, 4, "Answer")
	worksheet01.write(0, 5, "Answer Length")
	worksheet01.write(0, 6, "Question URL")

	row = 1

	for questionData in allExtractedDataList:
		for relatedQuestion in questionData['relatedQuestionData']:
			worksheet01.write(row, 0, questionData['initialQuestion'])
			worksheet01.write(row, 1, relatedQuestion['relatedQuestion'])
			worksheet01.write(row, 2, relatedQuestion['titleTag'])
			worksheet01.write(row, 3, relatedQuestion['titleTagLength'])
			worksheet01.write(row, 4, relatedQuestion['answer'])
			worksheet01.write(row, 5, relatedQuestion['answerLength'])
			worksheet01.write(row, 6, relatedQuestion['questionUrl'])
			row = row + 1

	workbook.close()

questions = ["Who do you think you are?", "Where do you get the nerve?", "What's your sob story?"]
pathToChromeDriver = "/path/to/chromedriver"
totalClicks = 10
driver = returnChromeDriver(pathToChromeDriver)

allExtractedDataList = []

for question in questions:
	driver = clickQuestions(driver, question, totalClicks)
	if driver.find_elements_by_css_selector('div.related-question-pair'):
		soup = BeautifulSoup(driver.page_source, "lxml")
		extractedData = extractQuestionData(soup)
		currentQuestionDict = {'initialQuestion':question, 'relatedQuestionData':extractedData} 
		allExtractedDataList.append(currentQuestionDict)

	else:
		print("No Questions Found For: " + question)

driver.quit()
