import os
from os import path
import pytest
from selenium.webdriver import Chrome, Firefox

from utils.constants import TestData
from utils.utils import MyLogger


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Type of browser: chrome, firefox")


@pytest.fixture(scope="session", autouse=True)
def add_binaries():
    current_dir = path.dirname(__file__)
    bin_dir = path.join(current_dir, "..", "bin")
    bin_dir = path.normpath(bin_dir)
    os.environ["PATH"] = ";".join((os.environ["PATH"], bin_dir))


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        browser_instance = Chrome()
    elif browser == "firefox":
        browser_instance = Firefox()
    else:
        raise ValueError

    yield browser_instance
    browser_instance.quit()


@pytest.fixture(scope="function")
def cleanup_browser(browser):
    browser.delete_all_cookies()
    return None


log = MyLogger().get_logger_custom(TestData.LOGGER_NAME_OF_THE_EXECUTED_TEST)


@pytest.fixture(autouse=True)
def get_name_of_each_test_for_logging(request):
    log.info(request.node.name)
