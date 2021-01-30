# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

import csv

# from selenium.webdriver.firefox.options import Options
# import random, re, requests
# import os

# options = Options()
# options.add_argument("--headless")
# options.add_argument("--disable-notifications")
# options.add_argument("disable-infobars")

driver = Firefox(executable_path='./driver/geckodriver.exe')
print('Firefox driver loaded')
wait = WebDriverWait(driver, 5)

def insert_link(file, link):
    with open(file, 'a+', newline='\n') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(link)
        print('link inserted')
        f.close()

for page in range(151,201):
    try:
        print("page %s"%(page))
        url = "https://www.mendeley.com/search/?page="+ str(page) +"&publicationType=journal&query=supply%20chain%20technology&sortBy=relevance"
        driver.implicitly_wait(15)
        sleep(5)
        driver.refresh()
        print('opening url...')
        driver.get(url)
        print('url opened')

        if page == 151:
            sleep(3)
            cookies = driver.find_element_by_id("onetrust-accept-btn-handler")
            cookies.click()
            print('cookies are accepted')

        journal = "/html/body/div[2]/main/div/div/div[3]/section/div/ol/div"
        results = driver.find_elements_by_xpath(journal)

        for j in range(1,11):
            wait.until(lambda driver: driver.find_element_by_xpath(journal))
            ax = "/html/body/div[2]/main/div/div/div[3]/section/div/ol/div[{}]".format(str(j))
            print("ax =", ax)
            driver.find_element_by_xpath(ax).click()
            sleep(3)
            href_elem = "/html/body/div[2]/main/aside/div[3]/div[2]/cite/a"
            wait.until(lambda driver: driver.find_element_by_xpath(href_elem))
            href = [driver.find_element_by_xpath(href_elem).get_attribute('href')]
            print(href[0])

            file = './data/urls-copy.csv'
            insert_link(file, href)
        
            sleep(3)
    except TimeoutException:
        sleep(60)
        driver.get(url)


    # sleep(5)
    # next_button = "/html/body/div[2]/main/div/div/div[3]/section/div/div[2]/button[3]"
    # driver.find_element_by_xpath(next_button).click()

    sleep(10)
