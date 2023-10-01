from pages.main_page import MainPage


URL = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, URL)
    page.open()
    page.go_to_login_page()