
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

query = input("Add query: ")
clicks = input("How many questions do you want to click? : ")
clicks = int(clicks)  # parse string into an integer


#This is only a loading bar



#Search Query and get results

options = Options()
options.headless = True

def search(query,clicks):
       with webdriver.Firefox() as driver:
            
            driver.get("https://www.google.com?hl=en")
            driver.find_element_by_xpath("//input[@aria-label='Search']").send_keys(query)
            driver.find_elements_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[3]/center/input[1]")
            searchbtn = driver.find_elements_by_xpath("//input[@aria-label='Google Search']")
            searchbtn[-1].click()
            
            #Questions with answers. Have to clean a little bit.
            
            paa = driver.find_elements_by_css_selector('div.related-question-pair')
            for i in range(clicks):
                paa[i].click()
                paa = driver.find_elements_by_css_selector('div.related-question-pair')
                for j in paa:
                        print(format(j.text))
            
                
        

    
search(query,clicks)






