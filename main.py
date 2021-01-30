from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
from crawlers.search import SearchPage
from crawlers.page import JournalPage
from time import sleep


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
        opts.add_argument("--headless")
        opts.add_argument("--disable-notifications")
        opts.add_argument("disable-infobars")

        driver = Firefox(executable_path='./driver/geckodriver.exe', options=opts)
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

