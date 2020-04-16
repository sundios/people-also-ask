
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time

query = input("Add query: ")


#Search Query and get results

def search(query):
    with webdriver.Firefox() as driver:
        driver.get("https://www.google.com?hl=en")
        driver.find_element_by_xpath("//input[@aria-label='Search']").send_keys(query)
        driver.find_elements_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[3]/center/input[1]")
        searchbtn = driver.find_elements_by_xpath("//input[@aria-label='Google Search']")
        searchbtn[-1].click()
        time.sleep(10)

               
        
        #clicking queestions
        questions = []
        for questions in driver.find_elements_by_xpath("//span/following-sibling::div[contains(@class,'match-mod-horizontal-padding')]"):
            questions.click()
            time.sleep(5)
            
        paa = driver.find_elements_by_xpath("//span/following-sibling::div[contains(@class,'match-mod-horizontal-padding')]")
        for i in paa:
            print(format(i.text))
        
        
search(query)



### This is for guidance

xpath("(//*[@id='menuitem'])[index]")


#x path by index??
(//div[@class='className'])[1]
(//div[@class='className'])[2]
(//div[@class='className'])[3]
(//div[@class='className'])[4]
(//div[@class='className'])[5]



persons = []
for person in driver.find_elements_by_class_name('person'):
    title = person.find_element_by_xpath('.//div[@class="title"]/a').text
    company = person.find_element_by_xpath('.//div[@class="company"]/a').text

    persons.append({'title': title, 'company': company})








