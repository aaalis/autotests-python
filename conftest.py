import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption('--lang', action='store', default=None,
                     help="Choose language: en or ru")


@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("lang")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    if lang != "en" and lang != "ru":
        raise pytest.UsageError("--lang should be ru or en")
    browser = webdriver.Chrome(options)
    yield browser
    browser.quit()
