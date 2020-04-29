
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from progress.bar import Bar

import itertools
import threading
import time
import sys

query = input("Add query: ")

done = False
#Loading Bar
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')


#Search Query and get results

options = Options()
options.headless = True

def search(query):
       t = threading.Thread(target=animate)
       t.start()
       with webdriver.Firefox(options=options) as driver:
            
            driver.get("https://www.google.com?hl=en")
            driver.find_element_by_xpath("//input[@aria-label='Search']").send_keys(query)
            driver.find_elements_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[3]/center/input[1]")
            searchbtn = driver.find_elements_by_xpath("//input[@aria-label='Google Search']")
            searchbtn[-1].click()
            time.sleep(3)
    
    #        #Questions separately
    #        paa = driver.find_elements_by_xpath("//span/following-sibling::div[contains(@class,'match-mod-horizontal-padding')]")
    #        
    #        #clicking Question 1 from here we need to figure out how to click each question and save childrens
    #        index = 0
    #        paa[index].click()
    #        time.sleep(3)
    #        paa = driver.find_elements_by_xpath("//span/following-sibling::div[contains(@class,'match-mod-horizontal-padding')]")
    #        
    #        for i in paa:
    #            print(format(i.text))
            
             #clicking questions
            questions = []
            for questions in driver.find_elements_by_xpath("//span/following-sibling::div[contains(@class,'match-mod-horizontal-padding')]"):
                questions.click()
                time.sleep(5)
                
            paa = driver.find_elements_by_xpath("//span/following-sibling::div[contains(@class,'match-mod-horizontal-padding')]")
            questions = []
            for i in paa:
                #print(format(i.text))
                q = format(i.text)
                questions.append(q)
            print(questions)
        

    
search(query)
done = True 
    
    
    


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







