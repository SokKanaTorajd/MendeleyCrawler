from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
# from selenium.webdriver.firefox.options import Options
import random, re, requests
import os

# options = Options()
# options.add_argument('-headless')
driver = Firefox(executable_path='C:/Users/acer/geckodriver.exe')
print('driver loaded')
journal_links = []

for i in range(1, 3):
    print('page %i'%(i))
    url = "https://www.mendeley.com/search/?page="+ str(i) +"&publicationType=journal&query=supply%20chain%20technology&sortBy=relevance"
    print(url)
    print('url opened')
    html_page = requests.get(url).content
    print('opening page')
    soup = BeautifulSoup(html_page, 'lxml')
    journals = soup.find_all('article', class_='ArticleCard__StyledArticleCard-sc-7btn0d-0 qbTmF')
    print(journals)
    print('title acquired')
    for journal in journals:
        driver.get(url)
        driver.find_element_by_class_name("ArticleCardTitle__TitleButton-sc-1jkrcs4-2 dTbwYc").click()
        print('button clicked')
        urls = journal.find_all("ArticleCardTitle__TitleLink-sc-1jkrcs4-1 ibfyqF")
        for url in urls:
            print('getting url...')
            link = url.get('href')
            link = "https://www.mendeley.com/"+str(link)
            print(link)
            journal_links.append(link)

driver.quit()
print(journal_links)