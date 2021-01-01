from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.firefox.options import Options
import random, re, requests
import os

# options = Options()
# options.add_argument("--headless")
# options.add_argument("--disable-notifications")
# options.add_argument("disable-infobars")
driver = Firefox(executable_path='C:/Users/acer/geckodriver.exe')
print('Firefox driver loaded')

# journal_links = []

# for i in range(1, 3):
#     print('page %i'%(i))
#     url = "https://www.mendeley.com/search/?page="+ str(i) +"&publicationType=journal&query=supply%20chain%20technology&sortBy=relevance"
#     print(url)
#     print('url opened')
#     html_page = requests.get(url).content
#     print('opening page')
#     soup = BeautifulSoup(html_page, 'lxml')
#     journals = soup.find_all('article', class_='ArticleCard__StyledArticleCard-sc-7btn0d-0 qbTmF')
#     print(journals)
#     print('title acquired')
#     for journal in journals:
#         driver.get(url)
#         driver.find_element_by_class_name("ArticleCardTitle__TitleButton-sc-1jkrcs4-2 dTbwYc").click()
#         print('button clicked')
#         urls = journal.find_all("ArticleCardTitle__TitleLink-sc-1jkrcs4-1 ibfyqF")
#         for url in urls:
#             print('getting url...')
#             link = url.get('href')
#             link = "https://www.mendeley.com/"+str(link)
#             print(link)
#             journal_links.append(link)

# print(journal_links)

for i in range(1,2):
    driver.implicitly_wait(15)
    print('opening url...')
    url = "https://www.mendeley.com/search/?page="+ str(i) +"&publicationType=journal&query=supply%20chain%20technology&sortBy=relevance"
    driver.get(url)
    print('url opened')
    driver.find_element_by_id("onetrust-accept-btn-handler").click()
    print('cookies are accepted')
    
    elem = "//article[@class='ArticleCard__StyledArticleCard-sc-7btn0d-0 qbTmF']"
    wait = WebDriverWait(driver, 7)
    wait.until(lambda driver: driver.find_element_by_xpath(elem))
    print('journal element acquired')
    driver.find_element_by_xpath(elem).click()
    print('a journal is clicked')

    href_elem = "//a[@class='ArticleCardTitle__TitleLink-sc-1jkrcs4-1 ibfyqF']"
    wait.until(lambda driver: driver.find_element_by_xpath(href_elem))
    print('href acquired')
    href = driver.find_element_by_xpath(href_elem).get_attribute('href')
    print("here's the link\n", href)

# driver.quit()
