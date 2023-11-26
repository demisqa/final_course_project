from pages.product_page import ProductPage
from selenium.webdriver.remote.webdriver import WebDriver


def test_guest_can_add_product_to_basket(browser : WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.compare_price_of_added_product_to_basket()
    product_page.compare_name_of_added_product_to_basket()