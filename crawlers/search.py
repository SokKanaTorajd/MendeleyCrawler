from selenium.common.exceptions import NoSuchElementException, TimeoutException
from crawlers.cookies import cookies_check
# from functions import insert_link
from data.database import DBModel
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

    # def get_links(self, url, file):
    def get_links(self,url):
        self.driver.implicitly_wait(10)
        print('opening url...')

        try:
            self.driver.get(url)
            self.driver.refresh()
            print('url opened')

            cookies_check(self.driver)
            
            journals_xpath = "/html/body/div[2]/main/div/div/div[3]/section/div/ol/div"
            results = self.driver.find_elements_by_xpath(journals_xpath)
            
            dbmodel = DBModel()
            collection = 'digital_supply_chain_urls'

            try:
                for i in range(len(results)):
                    self.driver.implicitly_wait(10)
                    jx = "/html/body/div[2]/main/div/div/div[3]/section/div/ol/div[{}]".format(str(i+1))
                    print("jx =", jx)
                    self.driver.find_element_by_xpath(jx).click()
                    # sleep(5)
                    href_elem = "/html/body/div[2]/main/aside/div[3]/div[2]/cite/a"
                    self.driver.implicitly_wait(10)

                    # ---- Save data in local
                    # link = [self.driver.find_element_by_xpath(href_elem).get_attribute('href')]
                    # insert_link(file, link)

                    # ---- Save data in server
                    
                    link = self.driver.find_element_by_xpath(href_elem).get_attribute('href')
                    value = dbmodel.check_docs(collection, link)
                    if value is False:
                        dbmodel.insert_url(collection, link)
                    else:
                        print('url is already inserted.')
                    sleep(3)
                    close_xpath = "//*[@id='root']/main/aside/div[3]/div[1]/button[3]"
                    self.driver.find_element_by_xpath(close_xpath).click()
                
                    sleep(5)

            except NoSuchElementException:
                print('Url is not acquired.')
            
            except TimeoutException:
                print('Taking too much time.')
        
        except NoSuchElementException:
            print('Cannot collect url, trying one more.')
            # self.get_links(url)

        except TimeoutException:
            print('Taking too much time, trying one more.')
            # self.get_links(url)
