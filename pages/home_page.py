from .base_page import BasePage
from .locators import HomePageLocators


class HomePage(BasePage):

    def should_be_present_slider_on_home_page(self):
        assert self.is_element_present(*HomePageLocators.SLIDER), "slider is not presented"
