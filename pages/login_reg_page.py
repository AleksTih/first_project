from .base_page import BasePage
from .locators import LoginRegLocators
from faker import Faker
fake = Faker()


class LoginRegPage(BasePage):
    def should_be_present_register_form(self):
        assert self.is_element_present(*LoginRegLocators.REG_FORM), "Registration form is not presented"

    def input_reg_name_and_email_and_go_to_step_two(self):
        self.browser.find_element(*LoginRegLocators.REG_NAME).send_keys("Alexandr")
        self.browser.find_element(*LoginRegLocators.REG_EMAIL).send_keys("autotest@mail.ru")
        self.browser.find_element(*LoginRegLocators.REG_BUTTON).click()

    def should_be_present_login_form(self):
        assert self.is_element_present(*LoginRegLocators.LOG_FORM), "Login form is not presented"

    def authorization_user(self):
        self.browser.find_element(*LoginRegLocators.LOG_EMAIL).send_keys("autotest@mail.ru")
        self.browser.find_element(*LoginRegLocators.LOG_PASS).send_keys("123456")
        self.browser.find_element(*LoginRegLocators.LOG_BUTTON).click()
