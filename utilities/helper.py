from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def wait_clickable(driver, locator, timeout=10):
    """
    Waits for an element to be clickable and clicks on it.

    :param driver: The WebDriver instance.
    :param locator: Locator tuple (By, value).
    :param timeout: Timeout for waiting. Defaults to 10 seconds.
    """
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
def wait_visible(driver, locator, timeout=10):
    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )
def wait_visible_all(driver, locator, timeout=10):
    WebDriverWait(driver, timeout).until(
        EC.visibility_of_all_elements_located(locator)
    )
def wait_invisible(driver, locator, timeout=10):
    WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located(locator)
    )
def wait_presence(driver, locator, timeout=10):
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )

def perform_action(driver, *locator):
    """
    Perform an action (like hovering) on a specified element.

    :param driver: The WebDriver instance.
    :param locator: Locator tuple (By, value).
    """
    # Find the element using the locator
    element = driver.find_element(locator[0], locator[1])

    # Create an ActionChains instance and perform the action
    action = ActionChains(driver)
    action.move_to_element(element).click().perform()



