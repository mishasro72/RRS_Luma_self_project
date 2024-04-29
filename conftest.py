import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException


@pytest.fixture
def chrome_opt():
    options = Options()
    options.add_argument('--windows size = 100, 100')
    options.add_argument('--headless')
    options.add_argument('--incognito')
    return options

@pytest.fixture
def driver(chrome_opt):
    print('\n Start testing')
    driver = webdriver.Chrome(options=chrome_opt)
    yield driver
    print('\n Finish testing')
    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout = 10)
    return wait
