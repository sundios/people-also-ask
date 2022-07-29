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
    
# Variables that user has to input

query = input("Add your query: ")
clicks = input("How many questions do you want to click?: ")
lang = input("Please select your languange. (For english type en. For spanish type es. For French type fr): ")
clicks = int(clicks)  # parse string into an integer






def search(query,clicks,lang):
    '''
    ----------
    query : string
        Query we want to look.
    clicks : int
        Number of times we will click on the question.
    lang :string
        Language we want the questions. Only English and Spanish

    Returns
    -------
    None.

    '''
    
    #headless option so it doesnt open chrome everytime we run it
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True

    driver = webdriver.Chrome(options=chrome_options,executable_path='/Users/konradburchadtpizarro-local/Desktop/chromedriver')  # Optional argument, if not specified will search path.
   
    driver.get("https://www.google.com?hl=" + lang)

    if lang == "en":
        print('The keyword you selected is:', query)
        print(' Number of clicks we will do is:',clicks)
        print('Language you selected is:',lang)

        driver.find_element_by_xpath("//input[@aria-label='Search']").send_keys(query+Keys.RETURN)
        print(query)
        clickingKW(clicks,driver)

    if lang =="es":
        print('The keyword you selected is:', query)
        print(' Number of clicks we will do is:',clicks)
        print('Language you selected is:',lang)
        
        driver.find_element_by_xpath("//input[@aria-label='Buscar']").send_keys(query+Keys.RETURN)
        print(query)
        clickingKW(clicks,driver)


def clickingKW(clicks,driver): 
    '''
    Function that clicks N Questions.

    Parameters
    ----------
    clicks : int
        number of clicks we will use on the questions
    driver : ?
        Driver that we are using

    Raises
    ------
    Exception
        If there are no questions to click then an exception will be raised

    Returns
    -------
    None.

    '''
    paa = driver.find_elements_by_class_name("related-question-pair")
    #Its range because clicks is int.
    for i in range(clicks):
        print('Clicking question #',i+1)
        try:
            paa[i].click()
            time.sleep( 2 )
            paa = driver.find_elements_by_class_name("wWOJcd")
            # for j in paa:
            #     print(format(j.text))
        except:
            continue
            raise Exception('There are no questions to Click! Index is out of Range. Please add another Keyword that contains questions')
    list_paa = [] 
    for j in paa:
        p = format(j.text)
        p = p.splitlines()
    
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