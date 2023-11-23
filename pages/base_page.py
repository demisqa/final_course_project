from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage():
    
    def __init__(self, browser : WebDriver, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, by, value):
        try:
            self.browser.find_element(by, value)
        except (NoSuchElementException):
            return False
        return True
