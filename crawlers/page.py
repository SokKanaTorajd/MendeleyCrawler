from selenium.common.exceptions import NoSuchElementException, TimeoutException
from crawlers.cookies import cookies_check
from functions import insert_detail
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
            xpath = "/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div[1]/h1"
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
            xpath = "//html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div[1]/div/ul/li"
            authors = self.driver.find_elements_by_xpath(xpath)
            auths = []
            for i in range(len(authors)):
                autx = "//html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div[1]/div/ul/li[{}]".format(str(i+1))
                authr = self.driver.find_element_by_xpath(autx).text
                auths.append(authr)
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

    def crawl_data(self, url_file, detail_file):
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
                self.driver.get(urls[i+1])

            detail = [urls[i], title, publisher, doc_id, auths, keys, abstract]
            print(detail)
            insert_detail(detail_file, detail)
            sleep(10)
        
        print('Journal Crawling Succeed')
