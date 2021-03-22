from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from tqdm import tqdm 
from time import sleep

import itertools
import threading
import time
import sys
import csv
import pandas as pd 

# query = "uber eats" Not being used

clicks = 4
clicks = int(clicks)  # parse string into an integer



#Search Query and get results

options = Options()
options.headless = True

def search(query,clicks):
       with webdriver.Firefox(options=options) as driver:
            driver.get("https://www.google.com?hl=en")
            driver.find_element_by_xpath("//input[@aria-label='Search']").send_keys(query)
            driver.find_elements_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[3]/center/input[1]")
            searchbtn = driver.find_elements_by_xpath("//input[@aria-label='Google Search']")
            searchbtn[-1].click()
            
            #Questions with answers. Have to clean a little bit.
            
            paa = driver.find_elements_by_css_selector('div.related-question-pair')
            for i in range(clicks):
                try:
                    paa[i].click()
                    paa = driver.find_elements_by_css_selector('div.related-question-pair')
                except IndexError as  k:
                    print('There are no questions to Click! Index is out of Range. Please add another Keyword that contains questions')
                pass
            list_paa = [] 
            for j in paa:
                    p = format(j.text)
                    p = p.splitlines()
                    
                    print(p)
                    list_paa.append(p)
                    
    
            df = pd.DataFrame(list_paa)
            
            df.to_csv( query + '.csv', index=False)
            
            
                    
""" File where we will save all keywords we want to run. Make sure the file is .xlsx and follows always the same format"""
df = pd.read_excel (r'keywords.xlsx')          

    
import time
from random import randint

for i in df['Keywords']:
    search(i,clicks)
    
    #Random sleep so that we dont get Google Captcha
    sleep = randint(1,20)
    print('Sleep time is', sleep)
    
    #Counter to show in terminal
    for k in range(sleep):
        sys.stdout.write(str(k)+' ')
        sys.stdout.flush()
        time.sleep(1)
        
""" Function that puts together all the CSV files into one big master file 'Biglist.csv'"""
def csv_concat():
    import os, glob
    import pandas as pd

    #Files that we want to run to get totals
    files = sorted(glob.glob('*.csv'))
    
    #opening all files and selecting 4 top rows and onoy 5 columns
    big_df = []
    for f in files: 
        #try & Except so that  we can keep going through the loop even if file has no columns.
        try:
            df = pd.read_csv(f,index_col=False)
            print(df)
            d = df.iloc[0:4,0:6]
            big_df.append(d)
        except:
            continue
        
    #merging all into one DF
    merged = pd.concat(big_df)
    
    merged.columns = ['Question','Answer','Answer 2',
                         'Title of page','URL','Search for question']
    
    
    #Exporting file into CSV
    merged.to_csv('Biglist.csv', index=False)
    
csv_concat()


            