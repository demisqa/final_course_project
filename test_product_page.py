import pytest
from pages.product_page import ProductPage
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
