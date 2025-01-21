import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utilities.helper import wait_visible
from utilities.locators import *

op = Options()
op.add_argument('--start-maximized')
op.add_argument("--incognito")
op.add_argument('--disable-notifications')

# Login Credentials -pass your parameters username and password
salesforce_username = ""
salesforce_password=""

@pytest.fixture(scope='function')
def setup():
    driver = webdriver.Chrome(options=op)
    driver.get("https://login.salesforce.com/")
    driver.find_element(*loginuser).send_keys(salesforce_username)
    driver.find_element(*loginpassword).send_keys(salesforce_password)
    driver.find_element(*login_button).click()
    wait_visible(driver,page_salesforce_header)
    yield driver
    driver.close()


def pytest_configure(config):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


