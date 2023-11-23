from pages.login_page import LoginPage


def test_user_can_do_signin_and_register(browser):
    link = "https://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
