from pages.login_page import LoginPage
from pages.main_page import MainPage

URL = "http://selenium1py.pythonanywhere.com/"
URL2 = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, URL)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


def test_guest_login_page(browser):
    page = LoginPage(browser, URL2)
    page.open()
    page.should_be_login_page()
