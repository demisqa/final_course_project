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
    
    def register_new_user(self, email, password):
        register_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        register_email.send_keys(email)

        register_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        register_password.send_keys(password)

        confirm_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        confirm_password.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
