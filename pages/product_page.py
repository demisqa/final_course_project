from .base_page import BasePage
from .locators import ProductPageLocators
import re


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


    def compare_price_of_added_product_to_basket(self):
        product_price_text = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price = self.extract_numeric_value(product_price_text)
        basket_price_text = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        basket_price = self.extract_numeric_value(basket_price_text)

        assert product_price == basket_price, f'Product price {product_price} '\
              f'do not equal price in basket {basket_price}'
    
    def compare_name_of_added_product_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        basket_product_name = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text
        
        assert product_name == basket_product_name, f'Product name {product_name} '\
              f'do not equal name in basket {basket_product_name}'
