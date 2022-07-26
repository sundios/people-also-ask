#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
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
from selenium.webdriver.common.by import By
# Variables that user has to input

query = input("Add your query: ")
clicks = input("How many questions do you want to click?: ")
lang = input("Please select your languange. (For english type en. For spanish type es. For French type fr): ")
clicks = int(clicks)  # parse string into an integer



""" Search function. It opens Google, adds query in search box clicks search. Then it looks for question box and clicks N times
each of the questions and prints them out. The more question it clicks the more answers we get

parameters: - query: Query we want to look.
            - clicks: number of times we will click on the question.
            - lang: Language we want the questions. Only English and Spanish
"""


def search(query,clicks,lang):
    
    #headless option so it doesnt open chrome everytime we run it
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = False

    driver = webdriver.Chrome(options=chrome_options,executable_path='C:/xampp/htdocs/paa/chromedriver.exe')  # Optional argument, if not specified will search path.
   
    driver.get("https://www.google.com?hl=" + lang)

    if lang == "en":
        print('The keyword you selected is:', query)
        print(' Number of clicks we will do is:',clicks)
        print('Language you selected is:',lang)

        driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(query+Keys.RETURN)
        print(query)
        clickingKW(clicks,driver)

    if lang =="es":
        print('The keyword you selected is:', query)
        print(' Number of clicks we will do is:',clicks)
        print('Language you selected is:',lang)
        
        driver.find_element(By.XPATH,"//input[@aria-label='Buscar']").send_keys(query+Keys.RETURN)
        print(query)
        clickingKW(clicks,driver)

"""Function that clicks N Questions.
Parameters: - clicks: number of clicks we will use on the questions
            - driver: Driver that we are using"""

def clickingKW(clicks,driver): 
    paa = driver.find_elements(By.CLASS_NAME,'r21Kzd')
    #Its range because clicks is int.
    time.sleep(2)
    for i in range(clicks):
        print('Clicking question #',i+1)
        try:
            paa[i].click()
            time.sleep(4)
            paa = driver.find_elements(By.CLASS_NAME,'r21Kzd')
            for j in paa:
              print(format(j.text))
            print(paa)
        except:
            continue
            raise Exception('There are no questions to Click! Index is out of Range. Please add another Keyword that contains questions')
    list_paa = [] 
    for j in paa:
        p = format(j.text)
        p = p.splitlines()
        print(p)
        list_paa.append(p)          

    df = pd.DataFrame(list_paa,columns=['Questions'])
    
    df = df.dropna()

#Error Handling when a query doesnt contain any questions. Error onoy occurs when dataframe is empty. Depending on Language we return different """
    if df.empty and lang == 'en':
        print('DataFrame is empty! There are no questions for your Keyword. Try a different keyword')
        data = [['No results. Please Try again or try a different Keyword','No Results','No Results']]
        df = pd.DataFrame(data,columns=['Questions','Sentiment','Magnitude'])
        print(df)

    if df.empty and lang == 'es':
        print('DataFrame vacio! No hay preguntas para tu Keyword. Porfavor intenta nuevamente con una keyword diferente')
        data = [['No hay resultados. Intenta nuevamente con una keyword diferente Please Try again or try a different Keyword','Sin Resultados','Sin Resultados']]
        df = pd.DataFrame(data,columns=['Questions','Sentiment','Magnitude'])
        print(df)

    elif lang == 'en':
        print(df)
        print('Visit https://simpletools.io to find more SEO tools like this.')
        df.to_csv(query+'.csv', index = False)

    elif lang == 'es':
        print(df)
        print('Visita https://simpletools.io para encontrar mas herramientas de SEO como esta')
        df.to_csv(query+'.csv', index = False)


search(query,clicks,lang)
