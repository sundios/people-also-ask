#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 23:28:11 2020

@author: konradburchardt
"""


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import pandas as pd
from random import randint
import time
import sys


# Variables that user has to input

query = input("Add your query: ")
clicks = input("How many questions do you want to click? : ")
lang = input("Please select your languange. (For english type en. For spanish type es. For French type fr) : ")
clicks = int(clicks)  # parse string into an integer


#headless option
options = Options()
options.headless = True

""" Search function. It opens Google, adds query in search box clicks search. Then it looks for question box and clicks N times
each of the questions and prints them out. The more question it clicks the more answers we get"""

def search(query,clicks,lang):
       with webdriver.Firefox(options=options) as driver:
           driver.get("https://www.google.com?hl=" + lang)

           #English
           if lang == "en":
                driver.find_element_by_xpath("//input[@aria-label='Search']").send_keys(query)
                driver.find_elements_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[3]/center/input[1]")
                searchbtn = driver.find_elements_by_xpath("//input[@aria-label='Google Search']")
                searchbtn[-1].click()

                #printing query
                print("Query is: ", query)

                #clicking questions
                clickingKW(clicks,driver)

            #Spanish
           if lang == "es":
                driver.find_element_by_xpath("//input[@aria-label='Buscar']").send_keys(query)
                driver.find_elements_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[3]/center/input[1]")
                searchbtn = driver.find_elements_by_xpath("//input[@aria-label='Buscar con Google']")
                searchbtn[-1].click()

                #printing query
                print("Palabra clave es: ", query)

                #clicking questions
                clickingKW(clicks,driver)

            #French
           if lang == "fr":
                driver.find_element_by_xpath("//input[@aria-label='Rech.']").send_keys(query)
                driver.find_elements_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[3]/center/input[1]")
                searchbtn = driver.find_elements_by_xpath("//input[@aria-label='Recherche Google']")
                searchbtn[-1].click()

                #Printing Query
                print("la requête est: ", query)

                #clicking questions
                clickingKW(clicks,driver)

"""Function that clicks N Questions from here we need to figure out how to click each question and save parent question and childrens"""

def clickingKW(clicks,driver):
    paa = driver.find_elements_by_xpath("//span/following-sibling::div[contains(@class,'match-mod-horizontal-padding')]")
    #Its range because clicks is int.
    for i in range(clicks):
        print(i)
        try:
            paa[i].click()
            paa = driver.find_elements_by_xpath("//span/following-sibling::div[contains(@class,'match-mod-horizontal-padding')]")
            for j in paa:
                print(format(j.text))
        except IndexError as  k:
            raise Exception('There are no questions to Click! Index is out of Range. Please add another Keyword that contains questions')


""" File where we will save all keywords we want to run. Make sure the file is .xlsx and follows always the same format"""
df = pd.read_excel (r'keywords.xlsx')

print('Your list of Keywords is:\n',df)

search(query,clicks,lang)

""" Loops that runs all the keywords from our File. This has a Random sleep time between 1 and 20 seconds
so that google doesnt give us a captcha if we do a high number of keywords"""

# for i in df['Keywords']:
#     search(i,clicks,lang)

#     #Random sleep so that we dont get Google Captcha
#     sleep = randint(1,20)
#     print('Sleep time is', sleep)

#     #Counter to show in terminal
#     for k in range(sleep):
#         sys.stdout.write(str(k)+' ')
#         sys.stdout.flush()
#         time.sleep(1)
