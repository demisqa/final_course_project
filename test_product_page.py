import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.parametrize('link',
    [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}"
     if i!=7 else pytest.param(7, marks=pytest.mark.xfail(reason="current offer does not work"))
     for i in range(10)])
def test_guest_can_add_product_to_basket(browser : WebDriver, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.compare_price_of_added_product_to_basket(product_page.get_price(),\
                                                          product_page.get_price_in_basket())
    product_page.compare_name_of_added_product_to_basket(product_page.get_product_name(),\
                                                         product_page.get_product_name_in_basket())

@pytest.mark.xfail(reason="failed according to task")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser : WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser : WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.xfail(reason="failed according to task")
def test_message_disappeared_after_adding_product_to_basket(browser : WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_disappear_success_message()

def test_guest_should_see_login_link_on_product_page(browser : WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser : WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_can_go_to_basket_page_from_product_page(browser : WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()

def test_guest_should_see_basket_link_on_product_page(browser : WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_basket_link()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser : WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_basket_is_empty()
    basket_page.should_be_empty_basket_message()
