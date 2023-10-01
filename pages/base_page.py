from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, browser: WebDriver, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, selector, value) -> bool:
        try:
            self.browser.find_element(selector, value)
        except (NoSuchElementException):
            return False
        return True

    def open(self):
        self.browser.get(self.url)
