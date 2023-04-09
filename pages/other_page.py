from .base_page import BasePage
from .locators import RegFormLocators
from .locators import DeleteAccountLocators
from .locators import CommonElements


class CreatedAccountPage(BasePage):
    def should_be_account_created_title(self):
        assert self.is_element_present(*RegFormLocators.CREATED_ACCOUNT_TITLE), "ACCOUNT CREATED title is not presented"
        self.browser.find_element(*CommonElements.CONTINUE_BUTTON).click()


class DeleteAccountPage(BasePage):
    def should_ba_delete_account_title(self):
        assert self.is_element_present(*DeleteAccountLocators.ACCOUNT_DELETE_TITLE), \
            "ACCOUNT DELETE title is not presented"
        self.browser.find_element(*CommonElements.CONTINUE_BUTTON).click()

