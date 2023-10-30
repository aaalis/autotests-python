from pages.login_page import LoginPage
from pages.main_page import MainPage

URL = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_login(browser):
    page = MainPage(browser, URL)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    login_page.login("test31@gmail.com", "testtest31")


# def test_guest_login_page(browser):
#     page = LoginPage(browser, URL2)
#     page.open()
#     page.should_be_login_page()
