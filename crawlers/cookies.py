from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep

def cookies_check(driver):
    try:
        driver.implicitly_wait(15)
        cookies = driver.find_element_by_id("onetrust-accept-btn-handler")
        cookies.click()
        print('\ncookies are accepted')
        sleep(3)
    except NoSuchElementException:
        print('\ncookies button unavailable')
        pass
    except TimeoutException:
        pass
    except TimeoutError:
        print('taking too much time')
        pass