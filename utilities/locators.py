from selenium.webdriver.common.by import By

# Login
loginuser =(By.CSS_SELECTOR, "#username")
loginpassword=(By.CSS_SELECTOR, "#password")
login_button=(By.CSS_SELECTOR, "#Login")
page_salesforce_header = (By.XPATH, "//h1/span[text()='Sales']")
salesforce_header =(By.XPATH, "//h1/span")
header_text = "Sales"
# New lead Creation
dropdown = (By.XPATH, "//one-app-nav-bar-item-root[@data-id='Lead']/one-app-nav-bar-item-dropdown")
new_lead = (By.XPATH,"//span[text()='New Lead']")
new_lead_modal =(By.CSS_SELECTOR, "[class='isModal inlinePanel oneRecordActionWrapper']")
salutation = (By.XPATH, "//span[text()='--None--']")
mr =(By.XPATH, "//lightning-base-combobox-item/span/span[text()='Mr.']")
lead_firstname =(By.XPATH, "//div/input[@placeholder='First Name']")
lead_lastname=(By.XPATH, "//div/input[@placeholder='Last Name']")
lead_company = (By.XPATH, "//input[@name='Company']")
save_button=(By.XPATH, "//button[text()='Save']")
# Validating new lead
# created_lead_from_dropdown = (By.XPATH,f"//span[text()='{fullname}']")
created_lead_from_dropdown= lambda firstname, lastname:(By.XPATH, f"//span[text()='{firstname} {lastname}']")
created_lead_name=(By.XPATH, "//lightning-formatted-name[@data-output-element-id='output-field']")
created_lead_status = (By.XPATH,"//records-record-layout-item[@field-label='Lead Status']//lightning-formatted-text[@slot='outputField']")

# lead Coversion nas new account
convert_button =(By.XPATH,"//div[@class='windowViewMode-normal oneContent active lafPageHost']//button[text()='Convert']")
create_new_account_button=(By.XPATH, "//span[normalize-space(text())='Create New Account']")
save_convert=(By.XPATH, '//div[@class="modal-footer slds-modal__footer"]/span/button')
window_close = (By.XPATH, "//button[@title='Close this window']")

# lead convertion validation
account_dropdown = (By.XPATH, "//one-app-nav-bar-item-root[@data-id ='Account']/one-app-nav-bar-item-dropdown")
created_account_from_dropdown =  lambda company:(By.XPATH, f"//span[text()='{company}']")
account_name_from_page=(By.XPATH, "//lightning-formatted-text[@slot='primaryField']")

# above account dropdown can be utilised for all account related activities
# Account Creation
new_account=(By.XPATH, "//span[text()='New Account']")
new_account_modal=(By.XPATH, "//div[@class='isModal inlinePanel oneRecordActionWrapper']//div/input[@class='slds-input' and @name='Name']")
account_save_button=(By.XPATH, "//button[text()='Save']")
account_name_locator=(By.XPATH, "//div/input[@class='slds-input' and @name='Name']")
modal_close =(By.XPATH, "//div[@class='isModal inlinePanel oneRecordActionWrapper']")

# Lead convertion to existing account
choose_existing_account =(By.XPATH,"//span[normalize-space(text())='Choose Existing Account']")
searching_matching_acc=(By.XPATH, "//div/input[@placeholder='Search for matching accounts']")
select_existing_acc=lambda account:(By.XPATH, f"//div[@class='listContent']/ul/li/a/div/div//mark[text()='{account}']")

# then for conversion via existing
contact_dropdown =(By.XPATH, "//one-app-nav-bar-item-root[@data-id ='Contact']/one-app-nav-bar-item-dropdown")
created_contact= lambda contact_name:(By.XPATH, f"//span[text()='{contact_name}']")
account_name_from_contact=(By.XPATH, "//records-record-layout-item[@field-label='Account Name']//records-hoverable-link//slot//slot")
contact_name_from_page=(By.XPATH, "//slot[@name='outputField']/lightning-formatted-name")

# Usecase2
# Account creation used earlier present xpaths
Opportunity_dropdown =  (By.XPATH, "//one-app-nav-bar-item-root[@data-id='Opportunity']/one-app-nav-bar-item-dropdown")
new_opportunity= (By.XPATH, "//span[text()='New Opportunity']")
opportunity_name_loc =(By.XPATH, "//div/input[@name='Name']")
new_account_list_appear=(By.XPATH,"//span/span/span[text()='New Account']")
list_of_acc_drop=(By.XPATH, "//ul/li//lightning-base-combobox-formatted-text")
accounts_list_box=(By.XPATH, "//input[@aria-haspopup='listbox']")
closedate_loc=(By.XPATH, "//div/input[@name='CloseDate']")
# Using the `By` approach (recommended)
stage_button = (By.XPATH, "//div/button[@aria-label='Stage']")
# Alternatively, using the string-based approach used for scrolling
stage_button_str = ("xpath", "//div/button[@aria-label='Stage']")
stage_list=lambda stage:(By.XPATH, f"//lightning-base-combobox-item//span[text()='{stage}']")
opportunity_save=(By.XPATH, "//div[@class='footer-full-width']//button[text()='Save']")
# contact earlier created
new_contact =(By.XPATH, "//span[text()='New Contact']")
contact_salute = (By.XPATH, "//button[@name='salutation']")
mr_loc =(By.XPATH, "//div/lightning-base-combobox-item/span/span[text()='Mr.']")
contact_last_name_loc=(By.XPATH, "//input[@name='lastName']")
acc_search_loc=(By.XPATH, "//input[@placeholder='Search Accounts...']")
select_acc_contact_attach = (By.XPATH, "//ul[@role='group']/li")
contact_save=(By.XPATH,"//runtime_platform_actions-action-renderer//button[text()='Save']")

# Verification of usecase2 then

created_opportunity=lambda opportunity_name:(By.XPATH, f"//span[text()='{opportunity_name}']")
opportunity_name_value=(By.XPATH,"//records-record-layout-item[@field-label='Opportunity Name']//lightning-formatted-text")
acc_name_from_oppo =(By.XPATH,"//records-record-layout-item[@field-label='Account Name']//records-hoverable-link//slot//slot")

# usecase_3
calender= (By.XPATH, "//one-app-nav-bar-item-root[@data-id ='Event']/a/span[text()='Calendar']")
new_event = (By.XPATH, "//button[text()='New Event']")
new_event_subject =(By.XPATH, "//div[@part='input-container']/input[@role='combobox']")
start_date = (By.XPATH, "//lightning-datepicker//input")
start_time = (By.XPATH, " //lightning-timepicker//lightning-base-combobox//input")
# moving the elemnt
search_acc_loc_str  = ("xpath", "//div/input[@placeholder='Search Accounts...']")
search_acc_loc =(By.XPATH, "//div/input[@placeholder='Search Accounts...']")
acc_select_in_event =lambda Account:(By.XPATH, f" //div[@class='listContent']/ul/li/a/div//span/mark[text()='{Account}']")
#
# //div[@class='listContent']/ul/li//lightning-formatted-rich-text/span[text()='{Account}']
event_save_button=(By.XPATH, "//div[@class='inlineFooter']//button/span[text()='Save']")

# Validating Events
collecting_year_values=(By.CSS_SELECTOR, "select[class='slds-select picklist__label']")
month_text =(By.XPATH, "//h2[@class='monthYear']")
next_month = (By.XPATH, "//a[@class='navLink nextMonth']")
click_date=lambda cal_date:(By.XPATH, f"//table[@class='calGrid']/tbody/tr/td[@data-datevalue='{cal_date}']")
meet_subject_loc_str=lambda subject:("xpath", f"//a[@data-id='subject-link' and text()='{subject}']")
meet_subject_loc=lambda subject:(By.XPATH, f"//a[@data-id='subject-link' and text()='{subject}']")
more_detail_button=(By.XPATH, "//a[text()='More Details']")
more_details=(By.LINK_TEXT, "More Details")
acc_name_event_page=(By.XPATH, "//runtime_hello_studio-related-record-detail//a")
details=(By.XPATH, "//span[text()='Details']")
event_name_from_details =(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Event.Subject']/div/dd/span")
time_details=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Event.StartDateTime']/div/dd/span")
