from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options as chrome_opts
from selenium.webdriver.firefox.options import Options as firefox_opts
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from crawlers.search import SearchPage
from crawlers.page import JournalPage
from data.database import DBModel
from time import sleep
import os


def get_browser(driver=None, launch_on=None):
    " driver='Chrome' or 'Firefox', launch='local' or 'server' "
    if driver == 'Firefox':
        fo = firefox_opts()
        fo.add_argument("--headless")
        fo.add_argument("--disable-notifications")
        fo.add_argument("disable-infobars")
        if launch_on == 'local':
            driver = Firefox(executable_path='./driver/geckodriver.exe', options=fo)
        else:
            firefox_opts.binary_location = os.environ.get("FIREFOX_BIN")
            driver = Firefox(executable_path=os.environ.get("GECKODRIVER_PATH"), options=fo)

    if driver == 'Chrome':
        co = chrome_opts()
        co.add_argument("--headless")
        co.add_argument("--disable-dev-shm-usage")
        co.add_argument("--no-sandbox")
        if launch_on == 'local':
            driver = Chrome(executable_path='./driver/chromedriver.exe', options=co)
        else:
            co.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
            driver  = Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=co)
    
    print('Loading driver...')
    return driver


# def collect_urls(driver, keyword, url_file):
def collect_urls(driver, keyword):
    driver.implicitly_wait(5)
    sp = SearchPage(driver)
    result = sp.insert_keyword(keyword)

    for i in range(int(result)):
        try:
            print('\npage {}'.format(i+1))
            url = 'https://www.mendeley.com/search/?page={}&publicationType=journal&query={}&sortBy=relevance'.format(i+1, keyword)
            # sp.get_links(url, url_file)
            sp.get_links(url)

        except TimeoutException:
            print('Wrong url or taking too much time to respond.')
            sp.get_links(url)

        except TimeoutError:
            print('Timeout. Trying one more time.')
            sp.get_links(url)

        sleep(5)


if __name__ == '__main__':
    try:
        driver = get_browser(driver='Chrome', launch_on='server')
        print('Driver opened.')
        
        # url_file = './data/urls.csv'
        # detail_file = './data/new-details.csv'

        # --- Collect Urls Command ---
        # keyword = 'digital supply chain'
        # collect_urls(driver, keyword)

        # # --- Collect Details Command ---
        jp = JournalPage(driver)
        dbmodel = DBModel()
        collection = 'digital_supply_chain_details'

        list_url = dbmodel.get_urls()
        for data in list_url:
            url = data['url']
            try:
                value = dbmodel.check_docs(collection, url)
                if value is False:
                    print("The url hasn't been crawled yet.")
                    jp.crawl_data(collection, url)
                else:
                    print("Url is already crawled.")

            except TimeoutError:
                print('Wrong url or taking too much time to respond.')
                jp.crawl_data(collection, url)

            except TimeoutException:
                print('Timeout. Trying one more time.')
                jp.crawl_data(collection, url)
            

        print('All data is collected')
        driver.close()
        print('Driver closed.')
    
    except KeyboardInterrupt:
        print('You have pressed Ctrl+C button.')
        driver.close()
        print('Driver closed.')

