import logging
from pytest_bdd import scenarios, given, when, then, parsers
import time
from utilities.locators import *
from utilities.helper import *

scenarios('../features/usecase_one.feature')

logger = logging.getLogger(__name__)
@given("Login to salesforce")
def login(setup):
    if setup.find_element(*salesforce_header).text == header_text:
        logger.info("Logged in Successfully")
    else:
        logger.info("Login Error")
# Lead Creation
@when(parsers.parse('Creating new lead as "{firstname}" "{lastname}" "{company}"'))
def creating_new_lead(setup,firstname,lastname,company):
    driver = setup
    time.sleep(1)
    wait_clickable(driver, dropdown)
    perform_action(driver, *dropdown)
    wait_clickable(driver, new_lead)
    perform_action(driver, *new_lead)
    wait_visible(driver, new_lead_modal)
    wait_clickable(driver, salutation)
    driver.find_element(*salutation).click()
    wait_clickable(driver, mr)
    driver.find_element(*mr).click()
    driver.find_element(*lead_firstname).send_keys(firstname)
    driver.find_element(*lead_lastname).send_keys(lastname)
    driver.find_element(*lead_company).send_keys(company)
    driver.find_element(*save_button).click()
    driver.execute_script("document.querySelector('.forceVisualMessageQueue').style.display='none';")
    logger.info("New Lead created")

@then(parsers.parse('Validating the lead with "{firstname}" "{lastname}"'))
def validating_lead(setup,firstname,lastname):
    fullname = firstname + ' ' + lastname
    time.sleep(1)  # created to load
    driver = setup
    wait_clickable(driver, dropdown)
    perform_action(driver, *dropdown)
    wait_clickable(driver, created_lead_from_dropdown(firstname, lastname))
    perform_action(driver, *created_lead_from_dropdown(firstname, lastname))
    logger.info("Created lead name: %s", driver.find_element(*created_lead_name).text)
    logger.info("Created Lead Status: %s",driver.find_element(*created_lead_status).text)
    if driver.find_element(*created_lead_name).text == "Mr. "+fullname:
            logger.info("Lead validation Completed successfully")
    else:
        logger.info("Created lead name doesn't match")
# Account Creation
@when(parsers.parse('Creating an account "{account_name}"'))
def creating_an_account(setup,account_name):
    time.sleep(1)
    driver = setup
    wait_clickable(driver, account_dropdown)
    perform_action(driver, *account_dropdown)
    wait_clickable(driver, new_account)
    perform_action(driver, *new_account)
    wait_visible(driver,new_account_modal)
    driver.find_element(*account_name_locator).send_keys(account_name)
    wait_clickable(driver,account_save_button)
    driver.find_element(*account_save_button).click()
    driver.execute_script("document.querySelector('.forceVisualMessageQueue').style.display='none';")
    wait_invisible(driver,modal_close)
    logger.info("Account creation step completed")

# then condition of account creation lead converted account creation are same as account is to be validated

@when(parsers.parse('Convert lead to account lead "{firstname}" "{lastname}"'))
def convert_to_account(setup,firstname,lastname):
    time.sleep(1)  # created to load
    driver = setup
    wait_clickable(driver, dropdown)
    perform_action(driver, *dropdown)
    wait_clickable(driver, created_lead_from_dropdown(firstname, lastname))
    perform_action(driver, *created_lead_from_dropdown(firstname, lastname))
    wait_visible(driver,convert_button)
    perform_action(driver, *convert_button)
    wait_visible(driver,create_new_account_button)
    driver.find_element(*create_new_account_button).click()
    driver.find_element(*save_convert).click()
    time.sleep(3)
    driver.save_screenshot("lead_convert.png")
    driver.find_element(*window_close).click()
    logging.info("Convert lead new account step completed")

@then(parsers.parse('Validating account created "{company}"'))
def validate_lead_Convert(setup,company):
    time.sleep(1)
    driver = setup
    wait_clickable(driver, account_dropdown)
    perform_action(driver,*account_dropdown)
    wait_clickable(driver, created_account_from_dropdown(company))
    perform_action(driver, *created_account_from_dropdown(company))
    wait_visible(driver,account_name_from_page)
    if company == driver.find_element(*account_name_from_page).text:
        logging.info("Account Validation Successful")

    else:
        logging.info("Account Validation Failed")

@when(parsers.parse('Convert lead to an existing "{account}" "{firstname}" "{lastname}"'))
def convert_to_existing_acc(setup,firstname,lastname,account):
    time.sleep(1)
    driver = setup
    wait_clickable(driver, dropdown)
    perform_action(driver, *dropdown)
    wait_clickable(driver, created_lead_from_dropdown(firstname, lastname))
    perform_action(driver, *created_lead_from_dropdown(firstname, lastname))
    wait_visible(driver, convert_button)
    perform_action(driver, *convert_button)
    wait_clickable(driver,choose_existing_account)
    perform_action(driver, *choose_existing_account)
    driver.find_element(*searching_matching_acc).send_keys(account)
    wait_clickable(driver,select_existing_acc(account))
    driver.find_element(*select_existing_acc(account)).click()
    driver.find_element(*save_convert).click()
    time.sleep(3)
    driver.save_screenshot("lead_convert_existing.png")
    driver.find_element(*window_close).click()
    logging.info("Convert lead existing account step completed")

@then(parsers.parse('Checking the new contact created : "{contact_name}" and account: "{account}"'))
def validate_event(setup,contact_name,account):
    time.sleep(1)
    driver = setup
    wait_clickable(driver,contact_dropdown)
    perform_action(driver,*contact_dropdown)
    wait_clickable(driver,created_contact(contact_name))
    perform_action(driver,*created_contact(contact_name))
    wait_clickable(driver,account_name_from_contact)
    acc_name = driver.find_element(*account_name_from_contact).text
    contact_page = driver.find_element(*contact_name_from_page).text
    if  contact_page == "Mr. " + contact_name and acc_name ==account:
        logging.info("Converted Lead validated contact name successfully")
    else:
        logging.info("Converted Lead validation failed")
