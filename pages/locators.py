from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_USERNAME_INPUT = (By.ID, 'id_login-username')
    LOGIN_PASS_INPUT = (By.ID, 'id_login-password')

    REG_FORM = (By.ID, 'register_form')
    REG_USERNAME_INPUT = (By.ID, 'id_registration-email')
    REG_PASS1_INPUT = (By.ID, 'id_registration-password1')
    REG_PASS2_INPUT = (By.ID, 'id_registration-password2')
