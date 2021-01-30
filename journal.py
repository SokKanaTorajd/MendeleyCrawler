from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
from crawlers.page import JournalPage
from crawlers.cookies import cookies_check
import pandas as pd
import csv

def insert_detail(file, detail):
    with open(file, 'a+', newline='\n', encoding="utf-8") as f:
        csv_write = csv.writer(f)
        csv_write.writerow(detail)
        print('detail inserted')
        f.close()

title_xpath = "/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div[1]/h1"
authors_xpath = "//html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div[1]/div/ul/li"
publisher_xpath = "/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div"
docId_xpath = "/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div[3]/a"
abstract_xpath = "/html/body/div[2]/div/div[2]/div/div[1]/div[1]/p/span"
keywords_xpath = "/html/body/div[2]/div/div[2]/div/div[1]/div[2]/ul/li"


df = pd.read_csv('./data/urls.csv')
urls = df['url']

# details = pd.read_csv('./data/details.csv') # , encoding='cp1252')
# url_details = details['url'].tolist()

driver = Firefox(executable_path='./driver/geckodriver.exe')
print('Firefox Driver Loaded')

jp = JournalPage(driver)

for i in range(len(urls)):
    # if urls[i] in url_details:
    #     print('%s is already inserted'%(urls[i]))

    # else:
    driver.implicitly_wait(10)
    driver.get(urls[i])
    driver.refresh()

    # Cookies Button Check
    cookies_check(driver)

    # Crawling Journal Page    
    try:
        title = jp.journal_title(title_xpath)
        publisher = jp.journal_publisher(publisher_xpath)
        doc_id = jp.journal_id(docId_xpath)
        auths = jp.journal_authors(authors_xpath)
        abstract = jp.journal_abstract(abstract_xpath)
        keys = jp.journal_keywords(keywords_xpath)
            
    except NoSuchElementException:
        urls[i] = driver.get(driver.current_url)
        print('url changed')

    # Save crawled data
    detail = [urls[i], title, publisher, doc_id, auths, keys, abstract]
    print(detail)
        
    file = './data/new-details.csv'
    insert_detail(file, detail)
    print()
    sleep(5)

print('Journal Crawling Succeed')    
driver.quit()