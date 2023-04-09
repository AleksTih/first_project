from .base_page import BasePage
from .locators import LoginRegLocators
from faker import Faker
fake = Faker()
import time



class LoginRegPage(BasePage):
    def should_be_present_register_form(self):
        assert self.is_element_present(*LoginRegLocators.REG_FORM), "Registration form is not presented"

    def input_reg_name_and_email_and_go_to_step_two(self):
        self.browser.find_element(*LoginRegLocators.REG_NAME).send_keys("Alexandr")
        self.browser.find_element(*LoginRegLocators.REG_EMAIL).send_keys(fake.email())
        self.browser.find_element(*LoginRegLocators.REG_BUTTON).click()

