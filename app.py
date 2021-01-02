from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.firefox.options import Options
import random, re, requests
import os

# options = Options()
# options.add_argument("--headless")
# options.add_argument("--disable-notifications")
# options.add_argument("disable-infobars")
driver = Firefox(executable_path='C:/Users/acer/geckodriver.exe')
print('Firefox driver loaded')

for i in range(1,2):
    driver.implicitly_wait(15)
    print('opening url...')
    url = "https://www.mendeley.com/search/?page="+ str(i) +"&publicationType=journal&query=supply%20chain%20technology&sortBy=relevance"
    driver.get(url)
    print('url opened')
    driver.find_element_by_id("onetrust-accept-btn-handler").click()
    print('cookies are accepted')

    wait = WebDriverWait(driver, 7)
    journal = "//li[@class='SearchResultItem__StyledSearchResultItem-sc-18hn6qj-0 fkuUBi qe-results-list']"
    results = driver.find_elements_by_xpath(journal)

    n = len(results)
    links = []
    for i in range(n):
        result = results[i].get_attribute('class')
        # print(result)
        wait.until(lambda driver: driver.find_element_by_xpath(journal))
        driver.find_element_by_xpath(journal).click()
        # print('a journal is clicked')

        href_elem = "//a[@class='ArticleCardTitle__TitleLink-sc-1jkrcs4-1 ibfyqF']"
        wait.until(lambda driver: driver.find_element_by_xpath(href_elem))
        # print('href acquired')
        href = driver.find_element_by_xpath(href_elem).get_attribute('href')
        print(href)
        for link in links:
            if link==href:
                pass
            else:
                links.append(href)
                

# driver.quit()
