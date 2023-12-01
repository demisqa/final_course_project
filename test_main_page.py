import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page_from_main_page(self, browser : WebDriver):
        link = "http://selenium1py.pythonanywhere.com/"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
    
    def test_guest_should_see_login_link_from_main_page(self, browser : WebDriver):
        link = "http://selenium1py.pythonanywhere.com/"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.should_be_login_link()

@pytest.mark.basket_guest
class TestBasketFromMainPage():
    def test_guest_can_go_to_basket_page_from_main_page(self, browser : WebDriver):
        link = "http://selenium1py.pythonanywhere.com/"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_url()
    
    def test_guest_should_see_basket_link_on_main_page(self, browser : WebDriver):
        link = "http://selenium1py.pythonanywhere.com/"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.should_be_basket_link()
    
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser : WebDriver):
        link = "http://selenium1py.pythonanywhere.com/"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.check_basket_is_empty()
        basket_page.should_be_empty_basket_message()
