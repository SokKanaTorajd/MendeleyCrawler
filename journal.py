from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep

import pandas as pd
import csv


title_xpath = "/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div[1]/h1"
authors_xpath = "//html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div[1]/div/ul/li"
publisher_xpath = "/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div"
docId_xpath = "/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div[3]/a"
abstract_xpath = "/html/body/div[2]/div/div[2]/div/div[1]/div[1]/p/span"
keywords_xpath = "/html/body/div[2]/div/div[2]/div/div[1]/div[2]/ul/li"

def insert_detail(file, detail):
    with open(file, 'a+', newline='\n', encoding="utf-8") as f:
        csv_write = csv.writer(f)
        csv_write.writerow(detail)
        print('detail inserted')
        f.close()

df = pd.read_csv('./data/urls-copy.csv')
urls = df['url']

details = pd.read_csv('./data/details.csv', encoding='cp1252')
url_details = details['url'].tolist()

driver = Firefox(executable_path='./driver/geckodriver.exe')
print('Firefox Driver Loaded')

for i in range(len(urls)):
    if urls[i] in url_details:
        print('%s is already inserted'%(urls[i]))

    else:
        driver.implicitly_wait(10)
        driver.get(urls[i])
        driver.refresh()

        try:
            cookies = driver.find_element_by_id("onetrust-accept-btn-handler")
            cookies.click()
            print('cookies are accepted')
            sleep(3)
        except NoSuchElementException:
            print('cookies button unavailable')
            pass
        
        try:
            title = driver.find_element_by_xpath(title_xpath).text
            print('title acquired')

            publisher = driver.find_element_by_xpath(publisher_xpath).text
            print('publisher acquired')

            try:
                doc_id = driver.find_element_by_xpath(docId_xpath).text
                print('doc_id acquired')
            except NoSuchElementException:
                doc_id = ''
                print('doc_id unavailable')
                pass

            abstract = driver.find_element_by_xpath(abstract_xpath).text
            print('abstract acquired')

            authors = driver.find_elements_by_xpath(authors_xpath)
            auths = []
            for i in range(len(authors)):
                aux = "//html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div[1]/div/ul/li[{}]".format(str(i+1))
                authr = driver.find_element_by_xpath(aux).text
                auths.append(authr)
            print('auhors acquired')

            keywords = driver.find_elements_by_xpath(keywords_xpath)
            keys = []
            for i in range(len(keywords)):
                keyx = "/html/body/div[2]/div/div[2]/div/div[1]/div[2]/ul/li[{}]".format(str(i+1))
                key_word = driver.find_element_by_xpath(keyx).text
                keys.append(key_word)
            print('keywords acquired')
            
        except NoSuchElementException:
            driver.get(driver.current_url)

        detail = [urls[i], title, publisher, doc_id, auths, keys, abstract]
        print(detail)
        
        file = './data/details.csv'
        insert_detail(file, detail)
        print()
        sleep(5)