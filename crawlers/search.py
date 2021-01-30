from selenium.common.exceptions import TimeoutException
from crawlers.cookies import cookies_check
from functions import insert_link
from time import sleep
import csv

class SearchPage():
    """
    Class Search is used for scrape journal links from search result
    """

    def __init__(self, driver):
        self.driver = driver

    def insert_keyword(self, keyword):
        url = 'https://www.mendeley.com/search/?page=1&publicationType=journal&query={}&sortBy=relevance'.format(keyword)
        self.driver.implicitly_wait(10)
        print('opening url...')
        self.driver.get(url)
        print('url opened')
        cookies_check(self.driver)
        sleep(5)
        page_xpath = '/html/body/div[2]/main/div/div/div[3]/section/div/div[2]/span'
        page = self.driver.find_element_by_xpath(page_xpath).text
        page = page.split()
        max_page = page[len(page)-1]
        return max_page

    def get_links(self, url, file):
        self.driver.implicitly_wait(15)
        print('opening url...')
        self.driver.get(url)
        self.driver.refresh()
        print('url opened')

        cookies_check(self.driver)

        journals_xpath = "/html/body/div[2]/main/div/div/div[3]/section/div/ol/div"
        results = self.driver.find_elements_by_xpath(journals_xpath)

        for i in range(len(results)):
            self.driver.implicitly_wait(10)
            jx = "/html/body/div[2]/main/div/div/div[3]/section/div/ol/div[{}]".format(str(i+1))
            print("jx =", jx)
            self.driver.find_element_by_xpath(jx).click()
            sleep(5)
            href_elem = "/html/body/div[2]/main/aside/div[3]/div[2]/cite/a"
            self.driver.implicitly_wait(10)
            link = [self.driver.find_element_by_xpath(href_elem).get_attribute('href')]

            insert_link(file, link)
        
            sleep(5)

