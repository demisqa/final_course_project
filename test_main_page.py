from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()