
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from progress.bar import Bar
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
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')
    
def Bar(seconds):
    for i in tqdm(range(seconds)):
        sleep(1)

    


#Search Query and get results

options = Options()
options.headless = True

def search(query,clicks):
       t = threading.Thread(target=animate)
       t.start()
       with webdriver.Firefox(options=options) as driver:
            
            driver.get("https://www.google.com?hl=en")
            driver.find_element_by_xpath("//input[@aria-label='Search']").send_keys(query)
            driver.find_elements_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[3]/center/input[1]")
            searchbtn = driver.find_elements_by_xpath("//input[@aria-label='Google Search']")
            searchbtn[-1].click()
            
            #Questions separately
            paa = driver.find_elements_by_xpath("//span/following-sibling::div[contains(@class,'match-mod-horizontal-padding')]")
            
    
            
            for i in range(clicks):
                Bar(1)
                print(i)
                paa[i].click()
                paa = driver.find_elements_by_xpath("//span/following-sibling::div[contains(@class,'match-mod-horizontal-padding')]")
                for j in paa:
                    print(format(j.text))
        

    
search(query,clicks)

done = True 





