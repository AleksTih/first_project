import time

from .pages.main_page import MainPage
from .pages.login_reg_page import LoginRegPage
from .pages.reg_form import RegistrationForm


def test_guest_can_go_to_login_page(browser):
    link = "https://automationexercise.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_present_slider_on_home_page()  # Проверка, что перешли на главную страницу
    page.go_to_login_page()  # Перешли на страницу логина и регистрации
    login_reg_page = LoginRegPage(browser, browser.current_url)
    login_reg_page.should_be_present_register_form()  # Проверяем наличие формы для регистрации
    login_reg_page.input_reg_name_and_email_and_go_to_step_two()  # Вводим имя и email и кликаем зарегистрировать
    registration_form_page = RegistrationForm(browser, browser.current_url)
    registration_form_page.should_be_present_register_title()  # Проверяем наличие заголовка "ENTER ACCOUNT INFORMATION"
    registration_form_page.form_filling_block_account_information()  # Заполняем блок "ENTER ACCOUNT INFORMATION"
    registration_form_page.form_filling_block_address_information()  # Заполняем блок "ADDRESS INFORMATION"
    # и создаём аккаунт
    time.sleep(10)
