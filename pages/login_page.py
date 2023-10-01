from pages.locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.__should_be_login_url()
        self.__should_be_login_form()
        self.__should_be_register_form()

    def __should_be_login_url(self):
        assert "login" in self.browser.current_url, "Url is not correct"

    def __should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not exist"

    def __should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not exist"
