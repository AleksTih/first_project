from .base_page import BasePage
from .locators import HomePageLocators
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def should_be_slider_present_in_home_page(self):
        assert self.is_element_present(*HomePageLocators.SLIDER), "Login link is not presented"