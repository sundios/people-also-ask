#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 00:21:42 2020

@author: konradburchardt
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import glob



query = input("Add your query: ")

def search(query):
    #URL to scrape data
    url = "https://www.google.com/search?q=" + query
    page = requests.get(url)
    
    #Parsing HTML
    soup = BeautifulSoup(page.text, 'html.parser')
    print(soup.prettify())
    
    paa = soup.findAll("div",{"class":"match-mod-horizontal-padding"})
    mydivs = soup.findAll("div", {"class": "match-mod-horizontal-padding"})
    print(mydivs)
search(query)