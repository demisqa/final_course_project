from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        url = self.browser.current_url
        assert "basket" in url,  f"Expected 'basket' in URL, but got {url}"

    def check_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORM)
    
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
