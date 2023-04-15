from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()

    def should_be_same_name(self):
        name_in_logged_as = self.browser.find_element(*MainPageLocators.NAME_LOGGED_AS).text
        assert name_in_logged_as != "Aleksandr", f"Incorrect logged name {name_in_logged_as}"

    def delete_account_button_click(self):
        self.browser.find_element(*MainPageLocators.DELETE_ACCOUNT).click()

    def logout_account_button_click(self):
        self.browser.find_element(*MainPageLocators.LOGOUT_ACCOUNT).click()

    def contact_us_button_click(self):
        self.browser.find_element(*MainPageLocators.CONTACT_US_BUTTON).click

