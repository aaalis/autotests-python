from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Link login is not presented"

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    # def go_to_login_page(self) -> LoginPage:
    #     link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     link.click()
    #     return LoginPage(browser=self.browser, url=self.browser.current_url)
