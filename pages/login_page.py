from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert "login" in url, f"Expected 'login' in URL, but got {url}"

    def should_be_login_form(self):
        assert self.browser.find_elements(*LoginPageLocators.LOGIN_FORM), "No login forms found on the page"

    def should_be_register_form(self):
        assert self.browser.find_elements(*LoginPageLocators.REGISTER_FORM), "No register forms found on the page"
