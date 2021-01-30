from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class LoginPage():
    """LoginPage is used for login into Mendeley Account"""

    def __init__(self, driver):
        self.driver = driver
    
    def login(self, email=None, password=None):
        email_elem = "//*[@id='bdd-email']"
        pwd_elem = "//*[@id='bdd-password']"
        ssi_elem = "//*[@id='bdd-staySignedIn']"

        login_url = "https://www.mendeley.com/sign/in/"
        self.driver.get(login_url)
        print('opening login page')
        self.driver.implicitly_wait(10)

        email_box = self.driver.find_element_by_xpath(email_elem)
        email_box.send_keys(email)
        self.driver.find_element_by_xpath("//*[@id='bdd-elsPrimaryBtn']").click()
        print('email inserted')
        sleep(5)

        WebDriverWait(self.driver, 7).until(lambda driver: driver.find_element_by_xpath(pwd_elem))
        pwd_box = self.driver.find_element_by_xpath(pwd_elem)
        pwd_box.send_keys(password)
        print('password inserted')

        ssi_checkbox = self.driver.find_element_by_xpath(ssi_elem).is_selected()
        if ssi_checkbox=='true':
            self.driver.find_element_by_xpath(ssi_elem).click()
        print('stay sign in unchecked')

        self.driver.find_element_by_xpath("//*[@id='bdd-elsPrimaryBtn']").click()
        print('login success')
        sleep(3)

