from selenium.common.exceptions import NoSuchElementException, TimeoutException
from crawlers.cookies import cookies_check
from functions import insert_detail
from data.database import DBModel
from pandas import read_csv
from time import sleep


class JournalPage():
    """
    Class Journal Page is used for scrape data of a journal page that exist in Mendeley Web.
    It will take Title, Authors, Publisher, Document ID (issn, doi), Abstract and Keyword.
    """

    def __init__(self, driver):
        self.driver = driver

    def journal_title(self):
        try:
            xpath = '//h1[@class="TitlePage-wu5tuy-0 GvTdT"]'
            title = self.driver.find_element_by_xpath(xpath).text
            print('title acquired')
        except NoSuchElementException:
            print('title unavailable')
            title = ''
            pass

        return title
    
    def journal_publisher(self):
        try:
            xpath = "/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div"
            publisher = self.driver.find_element_by_xpath(xpath).text
            print('publisher acquired')
        except NoSuchElementException:
            print('publisher unavailable')
            publisher = ''
            pass

        return publisher
    
    def journal_id(self):
        try:
            xpath = "/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div[3]/a"
            doc_id = self.driver.find_element_by_xpath(xpath).text
            print('doc_id acquired')
        except NoSuchElementException:
            doc_id = ''
            print('doc_id unavailable')
            pass
        
        return doc_id
    
    def journal_abstract(self):
        try:
            xpath = "/html/body/div[2]/div/div[2]/div/div[1]/div[1]/p/span"
            abstract = self.driver.find_element_by_xpath(xpath).text
            print('abstract acquired')
        except NoSuchElementException:
            print('abstract unavailable')
            abstract = ''
            pass
        
        return abstract
    
    def journal_authors(self):
        try:
            xpath = '//li[@class="ListItem-kfdxir-0 ListAuthor__ListAuthorItem-sc-1kigzp2-1 ljWowo"]'
            authors = self.driver.find_elements_by_xpath(xpath)
            auths = []
            for authr in authors:
                auths.append(authr.text)
            print('authors acquired')
        except NoSuchElementException:
            print('authors unavailable')
            auths = ''
            pass
            
        return auths
    
    def journal_keywords(self):
        try:
            xpath = '//li[@class="keywords__Item-o54tma-2 jSsgpj"]'
            keywords = self.driver.find_elements_by_xpath(xpath)
            keys = []
            for keyword in keywords:
                keys.append(keyword.text)
            print('keywords acquired')

        except NoSuchElementException:
            print('keywords unavailable')
            keys = ''
            pass
            
        return keys

    def crawl_local(self, url_file, detail_file):
        df = read_csv(url_file)
        urls = df['url']

        for i in range(len(urls)):
            self.driver.implicitly_wait(10)
            self.driver.get(urls[i])
            self.driver.refresh()

            # Cookies button check
            cookies_check(self.driver)

            # Crawling Journal Page
            try:
                title = self.journal_title()
                publisher = self.journal_publisher()
                doc_id = self.journal_id()
                auths = self.journal_authors()
                abstract = self.journal_abstract()
                keys = self.journal_keywords()

            except NoSuchElementException:
                urls[i] = self.driver.get(self.driver.current_url)
                print('url changed.\n')
            
            except TimeoutException:
                print('url {} unretrieved. Move to next url.\n'.format(urls[i]))
                detail = [self.driver.current_url, '', '', '', '', '', '']
                self.driver.get(urls[i+1])

            detail = [urls[i], title, publisher, doc_id, auths, keys, abstract]
            print(detail)
            insert_detail(detail_file, detail)
            sleep(10)
        
        print('Journal Crawling Succeed')

    def crawl_data(self, collection, url):
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        # self.driver.refresh()
        sleep(10)
        cookies_check(self.driver)

        dbmodel = DBModel()

        try:
            title = self.journal_title()
            publisher = self.journal_publisher()
            doc_id = self.journal_id()
            auths = self.journal_authors()
            abstract = self.journal_abstract()
            keys = self.journal_keywords()
            
            detail = [url, title, publisher, doc_id, auths, keys, abstract]
            dbmodel.insert_detail(collection, detail)

            print(detail, '\nDetail inserted.\n')
            sleep(10)

        except NoSuchElementException:
            detail = [self.driver.current_url, '', '', '', '', '', '']
            dbmodel.insert_detail(collection, detail)
            print('Cannot collect data, maybe wrong url.\n')
        
        except TimeoutException:
            detail = [self.driver.current_url, '', '', '', '', '', '']
            dbmodel.insert_detail(collection, detail)
            print('Take too much time. Move to next url.\n')
        
            
