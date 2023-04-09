from .base_page import BasePage
from .locators import RegFormLocators
from faker import Faker
from selenium.webdriver.support.ui import Select

fake = Faker()


class RegistrationFormPage(BasePage):
    def should_be_present_register_title(self):
        assert self.is_element_present(*RegFormLocators.REG_FORM_TITLE), "Registration form title is not presented"

    def form_filling_block_account_information(self):
        self.browser.find_element(*RegFormLocators.RADIOBUTTON_MR).click()
        self.browser.find_element(*RegFormLocators.REG_FORM_PASSWORD).send_keys("123456")
        Select(self.browser.find_element(*RegFormLocators.REG_FORM_SElECT_DAY)).select_by_value("10")
        Select(self.browser.find_element(*RegFormLocators.REG_FORM_SElECT_MONTH)).select_by_value("12")
        Select(self.browser.find_element(*RegFormLocators.REG_FORM_SElECT_YEARS)).select_by_value("1996")
        self.browser.find_element(*RegFormLocators.CHECKBOX_NEWSLETTER).click()
        self.browser.find_element(*RegFormLocators.CHECKBOX_SPECIAL_OFFERS).click()

    def form_filling_block_address_information(self):
        self.browser.find_element(*RegFormLocators.FIRST_NAME).send_keys(fake.first_name())
        self.browser.find_element(*RegFormLocators.LAST_NAME).send_keys(fake.last_name())
        self.browser.find_element(*RegFormLocators.COMPANY_NAME).send_keys(fake.company())
        self.browser.find_element(*RegFormLocators.COMPANY_ADDRESS).send_keys(fake.address())
        self.browser.find_element(*RegFormLocators.PERSON_ADDRESS).send_keys(fake.address())
        Select(self.browser.find_element(*RegFormLocators.COUNTRY)).select_by_value("United States")
        self.browser.find_element(*RegFormLocators.ZIPCODE).send_keys(fake.zipcode())
        self.browser.find_element(*RegFormLocators.PHONE_NUMBER).send_keys(fake.phone_number())
        self.browser.find_element(*RegFormLocators.REG_FORM_CREATE_ACCOUNT_BUTTON).click()





