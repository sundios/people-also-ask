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
from progress.bar import Bar
import time
import logging


query = input("Add query: ")
clicks = input("How many questions do you want to click? : ")
clicks = int(clicks)  # parse string into an integer




def search(query,clicks):
       with webdriver.Firefox() as driver:
            
            driver.get("https://www.google.com?hl=en")
            driver.find_element_by_xpath("//input[@aria-label='Search']").send_keys(query)
            driver.find_elements_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[3]/center/input[1]")
            searchbtn = driver.find_elements_by_xpath("//input[@aria-label='Google Search']")
            searchbtn[-1].click()
            
            #clicking Question 1 from here we need to figure out how to click each question and save childrens
            
            
            for i in range(clicks):
                print(i)
                paa[i].click()
                paa = driver.find_elements_by_xpath("//span/following-sibling::div[contains(@class,'match-mod-horizontal-padding')]")
                for j in paa:
                    print(format(j.text))

search(query,clicks)




            
        

    

    




#### This is for guidance
#
#xpath("(//*[@id='menuitem'])[index]")
#
#
##x path by index??
#(//div[@class='className'])[1]
#(//div[@class='className'])[2]
#(//div[@class='className'])[3]
#(//div[@class='className'])[4]
#(//div[@class='className'])[5]
#
#
#
#persons = []
#for person in driver.find_elements_by_class_name('person'):
#    title = person.find_element_by_xpath('.//div[@class="title"]/a').text
#    company = person.find_element_by_xpath('.//div[@class="company"]/a').text
#
#    persons.append({'title': title, 'company': company})
#







