import logging
from pytest_bdd import scenarios, given, when, then, parsers
import time
from datetime import datetime

from selenium.webdriver.support.select import Select

from utilities.locators import *
from utilities.helper import *

scenarios('../features/usecase_three.feature')

logger = logging.getLogger(__name__)
@given("Login to salesforce")
def login(setup):
    if setup.find_element(*salesforce_header).text == header_text:
        logger.info("Logged in Successfully")
    else:
        logger.info("Login Error")

@when(parsers.parse('Creating an event subject: "{subject}",date:"{input_date}",time:"{input_time}",Account: "{Account}"'))
def create_an_event(setup,subject,input_date,input_time,Account):
    driver = setup
    time.sleep(2)
    wait_visible_all(driver,calender)
    perform_action(driver,*calender)
    wait_clickable(driver,new_event)
    perform_action(driver, *new_event)
    wait_visible_all(driver, new_event_subject)
    driver.find_element(*new_event_subject).send_keys(subject)
    driver.find_element(*start_date).clear()
    driver.find_element(*start_date).send_keys(input_date)
    driver.find_element(*start_time).click()
    driver.find_element(*start_time).clear()
    driver.find_element(*start_time).send_keys(input_time)
    # selecting account
    acc = driver.find_element(*search_acc_loc_str)
    driver.execute_script("arguments[0].scrollIntoView(true);", acc)
    driver.find_element(*search_acc_loc).send_keys(Account)
    wait_visible_all(driver,acc_select_in_event(Account))
    driver.find_element(*acc_select_in_event(Account)).click()
    driver.find_element(*event_save_button).click()
    driver.execute_script("document.querySelector('.forceVisualMessageQueue').style.display='none';")
    logger.info("Event created as expected")

@then(parsers.parse('Validating the event subject: "{subject}",date:"{input_date}",time:"{input_time}",Account: "{Account}"'))
def validate_event(setup,subject,input_date,input_time,Account):
    driver = setup
    time.sleep(2)
    date_obj = datetime.strptime(input_date, "%d-%b-%Y")
    day = str(date_obj.day)
    year_value = str(date_obj.year)
    month = date_obj.strftime("%B").upper()
    cal_date = date_obj.strftime("%Y-%m-%d")
    year = Select(driver.find_element(*collecting_year_values))
    year.select_by_visible_text(year_value)
    while month != driver.find_element(*month_text).text:
        driver.find_element(*next_month).click()

    driver.find_element(*click_date(cal_date)).click()
    time.sleep(1)
    element = driver.find_element(*meet_subject_loc_str(subject))
    # Scroll to the element
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    driver.find_element(*meet_subject_loc(subject)).click()
    wait_visible(driver,more_detail_button)
    driver.find_element(*more_details).click()
    wait_visible(driver,acc_name_event_page)
    acc_page = driver.find_element(*acc_name_event_page).text
    driver.find_element(*details).click()
    wait_visible(driver, event_name_from_details)
    event_name = driver.find_element(*event_name_from_details).text
    timing =driver.find_element(*time_details).text

    if timing == f"{date_obj.strftime('%d/%m/%Y')}, {input_time}" and event_name == subject and acc_page==Account:
            logger.info("Event created and Validated meeting name,time,account successfully")

    else:
        logger.info("Event Validation failed")