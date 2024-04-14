
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.CheckoutPageLocators import CheckoutPageLocators
from ssqatest.src.helpers.generic_helpers import generate_random_email_and_password
from ssqatest.src.helpers.config_helpers import get_base_url
import selenium
selenium.__version__
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions
driver = webdriver.Chrome(service = service, options = options)
class CheckoutPage(CheckoutPageLocators):

    def __init__(self):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def input_billing_first_name(self, first_name=None):
        first_name = first_name if first_name else 'AutomationFname'
        self.sl.wait_and_input_text(self.BILLING_FIRST_NAME_FIELD, first_name)

    def input_billing_last_name(self,last_name=None):
        last_name = last_name if last_name else 'AutomationLname'
        self.sl.wait_and_input_text(self.BILLING_LAST_NAME_FIELD, last_name)

    def input_billing_street_address(self, address1=None):
        address1 = address1 if address1 else "123 Main St."

    def input_billing_city(self, city=None):
        city = 'San Francisco' if not city else city
        self.sl.wait_and_input_text(self.BILLING_CITY_FIELD, city)

    def input_billing_zip(self,  zip_code=None):
        zip_code = 94016 if not zip_code else zip_code
        self.sl.wait_and_input_text(self.BILLING_ZIP_FIELD, zip_code)

    def input_billing_phone_number(self, phone=None):
        phone = '4151111111' if not phone else phone
        self.sl.wait_and_input_text(self.BILLING_PHONE_FIELD, phone)

    def input_billing_email(self, email=None):
        if not email:
            rand_email = generate_random_email_and_password()
            email = rand_email['email']
        self.sl.wait_and_input_text(self.BILLING_EMAIL_FIELD, email)

    def fill_in_billing_info(self, f_name = None, l_name=None, street1=None, city=None, zip_code=None, phone = None, email=None):
        self.input_billing_first_name(first_name=f_name)
        self.input_billing_last_name(last_name=l_name)
        self.input_billing_street_address(address1=street1)
        self.input_billing_city(city=city)
        self.input_billing_zip(zip_code = zip_code)
        self.input_billing_phone_number(phone=phone)
        self.input_billing_email(email=email)

    def click_on_place_order(self):
        self.sl.wait_and_click(self.PLACE_ORDER_BUTTON)














# class CheckoutPage(CheckoutPageLocators):
#
#     endpoint = '/checkout'
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.sl = SeleniumExtended(self.driver)
#
#     def go_to_checkout_page(self):
#         base_url = get_base_url()
#         checkout_url = base_url + self.endpoint
#         self.driver.get(checkout_url)
#
#     def input_billing_first_name(self, first_name=None):
#         first_name = first_name if first_name else 'AutomationFname'
#         self.sl.wait_and_input_text(self.BILLING_FIRST_NAME_FIELD, first_name)
#
#     def input_billing_last_name(self, last_name=None):
#         last_name = last_name if last_name else 'AutomationLname'
#         self.sl.wait_and_input_text(self.BILLING_LAST_NAME_FIELD, last_name)
#
#     def input_billing_street_address_1(self, address1=None):
#         address1 = address1 if address1 else "123 Main st."
#         self.sl.wait_and_input_text(self.BILLING_ADDRESS_1_FIELD, address1)
#
#     def input_billing_city(self, city=None):
#         city = 'San Francisco' if not city else city
#         self.sl.wait_and_input_text(self.BILLING_CITY_FIELD, city)
#
#     def input_billing_zip(self,  zip_code=None):
#         zip_code = 94016 if not zip_code else zip_code
#         self.sl.wait_and_input_text(self.BILLING_ZIP_FIELD, zip_code)
#
#     def input_billing_phone_number(self, phone=None):
#         phone = '4151111111' if not phone else phone
#         self.sl.wait_and_input_text(self.BILLING_PHONE_FIELD, phone)
#
#     def input_billing_email(self, email=None):
#         if not email:
#             rand_email = generate_random_email_and_password()
#             email = rand_email['email']
#         self.sl.wait_and_input_text(self.BILLING_EMAIL_FIELD, email)
#
#     def select_billing_country(self, country="Ethiopia"):
#         self.sl.wait_and_select_dropdown(self.BILLING_COUNTRY_DROPDOWN, to_select=country, select_by="visible_text")
#
#     def select_billing_state(self, state='California'):
#         self.sl.wait_and_select_dropdown(self.BILLING_STATE_DROPDOWN, to_select=state, select_by="visible_text")
#
#
#     def fill_in_billing_info(self, f_name=None, l_name=None, street1=None, city=None, zip_code=None, phone=None, email=None, state=None):
#         self.input_billing_first_name(first_name=f_name)
#         self.input_billing_last_name(last_name=l_name)
#         self.input_billing_street_address_1(address1=street1)
#         self.input_billing_city(city=city)
#         self.input_billing_zip(zip_code=zip_code)
#         self.input_billing_phone_number(phone=phone)
#         self.input_billing_email(email=email)
#         self.select_billing_country()
#         self.select_billing_state(state="Nevada")
#
#     def click_place_order(self):
#         self.sl.wait_and_click(self.PLACE_ORDER_BTN)
#
#
# class CheckoutPage(CheckoutPageLocators):
#     def select_country_dropdown(self, country):
#         country = 'US' if not country else country
#         self.sl.wait_and_select_dropdown(self.BILLING_COUNTRY_DROPDOWN, to_select=country, select_by="visible_test")
#     def select_state_dropdown(self, state):
#         state = 'Alabama' if not state else state
#         self.sl.wait_and_select_dropdown(self.BILLING_STATE_DROPDOWN, to_select=state, select_by="visible_test")
#
#     def fill_in_billing_info(self, f_name=None, l_name=None, country=None, state=None, street1=None, city=None, zip_code=None, phone=None, email=None):
#         self.select_country_dropdown(country=country)
#         self.select_state_dropdown(state=state)