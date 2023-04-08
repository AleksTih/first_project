from .base_page import BasePage
from .locators import HomePageLocators


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*HomePageLocators.LOGIN_LINK).click()

    def should_be_present_slider_on_home_page(self):
        assert self.is_element_present(*HomePageLocators.SLIDER), "slider is not presented"
