from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from crawlers.search import SearchPage
from crawlers.page import JournalPage
from time import sleep
import os


def collect_urls(driver, keyword, url_file):
    driver.implicitly_wait(5)
    result = sp.insert_keyword(keyword)

    for i in range(int(result)):
        print('\npage {}'.format(i+1))
        url = 'https://www.mendeley.com/search/?page={}&publicationType=journal&query={}&sortBy=relevance'.format(i+1, keyword)
        sp.get_links(url, url_file)
        sleep(20)


if __name__ == '__main__':
    try:
        opts = Options()
        # opts.add_argument("--headless")
        # opts.add_argument("--disable-notifications")
        # opts.add_argument("disable-infobars")
        # opts.binary_location = os.environ.get("FIREFOX_BIN")
        # driver = Firefox(executable_path='./driver/geckodriver.exe', options=opts)
        # driver = Firefox(executable_path=os.environ.get("GECKODRIVER_PATH"), options=opts)

        opts.add_argument("--headless")
        opts.add_argument("--disable-dev-shm-usage")
        opts.add_argument("--no-sandbox")
        opts.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        driver  = Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=opts)

        print('Firefox driver loaded')
        sp = SearchPage(driver)
        keyword = 'supply chain'
        url_file = './data/urls.csv'
        detail_file = './data/new-details.csv'

        # Collect Urls Command
        # collect_urls(driver, keyword, url_file)

        # Collect Details Command
        jp = JournalPage(driver)
        jp.crawl_data(url_file, detail_file)
        driver.close()
    
    except KeyboardInterrupt:
        print('You have pressed Ctrl+C button.')
        driver.close()
        print('Driver closed.')

