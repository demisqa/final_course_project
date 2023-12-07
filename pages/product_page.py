import re
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        product_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        product_button.click()

    def extract_numeric_value(self, text_price):
        match = re.search(r'\d+(\.\d+)?', text_price.replace(',', '.'))
        if match:
            return float(match.group())
        else:
            return None
    
    def get_price(self):
        product_price_text = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price = self.extract_numeric_value(product_price_text)
        return product_price
    
    def get_price_in_basket(self):
        basket_price_text = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        basket_price = self.extract_numeric_value(basket_price_text)
        return basket_price
    
    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def get_product_name_in_basket(self):
        basket_product_name = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text
        return basket_product_name

    def compare_price_of_added_product_to_basket(self, product_price, basket_price):
        assert product_price == basket_price, f'Product price {product_price} '\
              f'do not equal price in basket {basket_price}'
    
    def compare_name_of_added_product_to_basket(self, product_name, basket_product_name):
        assert product_name == basket_product_name, f'Product name {product_name} '\
              f'do not equal name in basket {basket_product_name}'
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should not be"
    
    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should disappear"
        
    def should_be_basket_name_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRODUCT_NAME, timeout=6),\
            "Name of added product to basket is not available on message"

    def should_be_basket_price_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE, timeout=6),\
            "Price of added product to basket is not available on message"
    
    def should_be_all_adding_messages(self):
        self.should_be_basket_name_message()
        self.should_be_basket_price_message()
