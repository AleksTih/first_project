import time
from .pages.home_page import HomePage
from .pages.main_page import MainPage
from .pages.login_reg_page import LoginRegPage
from .pages.reg_form import RegistrationFormPage
from .pages.other_page import CreatedAccountPage
from .pages.other_page import DeleteAccountPage


def test_registration_user(browser):
    link = "https://automationexercise.com/"
    home_page = HomePage(browser, link)
    home_page.open()
    home_page.should_be_present_slider_on_home_page()  # Проверка, что перешли на главную страницу
    main_page = MainPage(browser, link)
    main_page.go_to_login_page()  # Перешли на страницу логина и регистрации
    login_reg_page = LoginRegPage(browser, browser.current_url)
    login_reg_page.should_be_present_register_form()  # Проверяем наличие формы для регистрации
    login_reg_page.input_reg_name_and_email_and_go_to_step_two()  # Вводим имя и email и кликаем зарегистрировать
    registration_form_page = RegistrationFormPage(browser, browser.current_url)
    registration_form_page.should_be_present_register_title()  # Проверяем наличие заголовка "ENTER ACCOUNT INFORMATION"
    registration_form_page.form_filling_block_account_information()  # Заполняем блок "ENTER ACCOUNT INFORMATION"
    registration_form_page.form_filling_block_address_information()  # Заполняем блок "ADDRESS INFORMATION"
    # и создаём аккаунт
    created_account_page = CreatedAccountPage(browser, browser.current_url)
    created_account_page.should_be_account_created_title()  # Проверяем наличие заголовка "ACCOUNT CREATED!"
    # и нажали кнопку "Continue"
    main_page.should_be_same_name()  # Проверяем, что отображается «Вход в систему 'имя пользователя'».
    main_page.delete_account_button_click()
    delete_account_page = DeleteAccountPage(browser, browser.current_url)
    delete_account_page.should_ba_delete_account_title()  # Проверяем наличие заголовка "ACCOUNT DELETED!"
    # и нажали кнопку "Continue"
    time.sleep(10)
