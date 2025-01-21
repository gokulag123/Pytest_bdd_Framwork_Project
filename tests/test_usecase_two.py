import logging
from pytest_bdd import scenarios, given, when, then, parsers
import time
from utilities.locators import *
from utilities.helper import *

scenarios('../features/usecase_two.feature')

logger = logging.getLogger(__name__)
@given("Login to salesforce")
def login(setup):
    if setup.find_element(*salesforce_header).text == header_text:
        logger.info("Logged in Successfully")
    else:
        logger.info("Login Error")

# Account creation attach contact and Opportunity
@when(parsers.parse('Create an account: "{account}" attach opportunity: "{opportunity_name}" and contact: "{contact_name}",close_date: "{closedate}",Stage: "{stage}"'))
def creating_account_oppo_contact(setup,closedate,account,contact_name,opportunity_name,stage):
    driver = setup
    time.sleep(2)
    wait_clickable(driver, account_dropdown)
    perform_action(driver, *account_dropdown)
    wait_clickable(driver, new_account)
    perform_action(driver, *new_account)
    wait_visible(driver, new_account_modal)
    driver.find_element(*account_name_locator).send_keys(account)
    wait_clickable(driver, account_save_button)
    driver.find_element(*account_save_button).click()
    driver.execute_script("document.querySelector('.forceVisualMessageQueue').style.display='none';")
    wait_invisible(driver, modal_close)
    logger.info("Account creation step completed")
    # Creating an oPPortunity and attaching to account
    time.sleep(2)
    wait_clickable(driver,Opportunity_dropdown)
    perform_action(driver, *Opportunity_dropdown)
    wait_clickable(driver, new_opportunity)
    perform_action(driver, *new_opportunity)
    wait_clickable(driver,opportunity_name_loc)
    driver.find_element(*opportunity_name_loc).send_keys(opportunity_name)
    driver.find_element(*accounts_list_box).send_keys(account)
    wait_visible(driver,new_account_list_appear)
    accounts_list = driver.find_elements(*list_of_acc_drop)
    # selecting account from the list
    for acc in accounts_list:
        if acc.text == account:
            acc.click()
            break

    driver.find_element(*closedate_loc).send_keys(closedate)  # "31/12/2025"
    # Locate the element
    element = driver.find_element(*stage_button_str)
    # Scroll to the element
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    driver.find_element(*stage_button).click()
    wait_clickable(driver,stage_list(stage))
    perform_action(driver,*stage_list(stage))
    driver.find_element(*opportunity_save).click()
    logger.info("Opportunity Attached")
    # contact attachment
    time.sleep(1)
    wait_clickable(driver, contact_dropdown)
    perform_action(driver, *contact_dropdown)
    wait_clickable(driver, new_contact)
    perform_action(driver, *new_contact)
    wait_clickable(driver,contact_salute)
    driver.find_element(*contact_salute).click()
    wait_clickable(driver,mr_loc)
    driver.find_element(*mr_loc).click()
    driver.find_element(*contact_last_name_loc).send_keys(contact_name)
    driver.find_element(*acc_search_loc).send_keys(account)
    wait_visible(driver, new_account_list_appear)
    account_lis = driver.find_elements(*select_acc_contact_attach)
    for acc in account_lis:
        if acc.text == account:
            acc.click()
            break

    driver.find_element(*contact_save).click()
    logger.info("Account created Opportunity and contact Attached")

@then(parsers.parse('Validate these account: "{account}" attach opportunity: "{opportunity_name}" and contact: "{contact_name}"'))
def validate_acc_oppo_cont(setup,contact_name,account,opportunity_name):
    driver =setup
    time.sleep(2)  ##Then only it will show in recent accounts    #removed fails#
    wait_clickable(driver, account_dropdown)
    perform_action(driver, *account_dropdown)
    wait_clickable(driver, created_account_from_dropdown(account))
    perform_action(driver, *created_account_from_dropdown(account))
    wait_visible(driver, account_name_from_page)
    if account == driver.find_element(*account_name_from_page).text:
        logging.info("Account Validation Successful")

    else:
        logging.info("Account Validation Failed")
    time.sleep(1)
    # Opportunity check
    wait_clickable(driver, Opportunity_dropdown)
    perform_action(driver, *Opportunity_dropdown)
    wait_clickable(driver, created_opportunity(opportunity_name))
    perform_action(driver, *created_opportunity(opportunity_name))
    wait_visible(driver,acc_name_from_oppo)
    acc_name = driver.find_element(*acc_name_from_oppo).text
    oppo_name_page = driver.find_element(*opportunity_name_value).text
    if acc_name == account and oppo_name_page == opportunity_name:
        logging.info("Opportunity Validation Successful")
    else:
        logging.info("Opportunity Validation failed")
    time.sleep(1)
    # contact check
    driver = setup
    wait_clickable(driver, contact_dropdown)
    perform_action(driver, *contact_dropdown)
    wait_clickable(driver, created_contact(contact_name))
    perform_action(driver, *created_contact(contact_name))
    wait_presence(driver, contact_name_from_page)
    contact_page = driver.find_element(*contact_name_from_page).text
    wait_presence(driver, account_name_from_contact)
    acc_name = driver.find_element(*account_name_from_contact).text

    if contact_page == "Mr. " + contact_name and acc_name ==account:
        logging.info("Contact and Opportunity has been attached to Account successfully")
    else:
        logging.info("Contact and Opportunity has been attaching failed")



