from selenium.webdriver.common.by import By


class HomePageLocators:
    SLIDER = (By.CSS_SELECTOR, "section#slider")
    LOGIN_LINK = (By.CSS_SELECTOR, ".fa.fa-lock")


class LoginRegLocators:
    REG_FORM = (By.CSS_SELECTOR, ".signup-form")
    REG_NAME = (By.CSS_SELECTOR, "[data-qa = 'signup-name']")
    REG_EMAIL = (By.CSS_SELECTOR, "[data-qa = 'signup-email']")
    REG_BUTTON = (By.CSS_SELECTOR, "[data-qa = 'signup-button']")


class RegFormLocators:
    REG_FORM_TITLE = (By.XPATH, "//b[contains(text(),'Enter Account Information')]")
    RADIOBUTTON_MR = (By.CSS_SELECTOR, "#id_gender1")
    REG_FORM_PASSWORD = (By.CSS_SELECTOR, "#password")
    REG_FORM_SElECT_DAY = (By.CSS_SELECTOR, "#days")
    REG_FORM_SElECT_MONTH = (By.CSS_SELECTOR, "[data-qa = 'months']")
    REG_FORM_SElECT_YEARS = (By.CSS_SELECTOR, "#years")
    CHECKBOX_NEWSLETTER = (By.CSS_SELECTOR, "#newsletter")
    CHECKBOX_SPECIAL_OFFERS = (By.CSS_SELECTOR, "#optin")
    FIRST_NAME = (By.CSS_SELECTOR, "#first_name")
    LAST_NAME = (By.CSS_SELECTOR, "#last_name")
    COMPANY_NAME = (By.CSS_SELECTOR, "#company")
    COMPANY_ADDRESS = (By.CSS_SELECTOR, "#address1")
    PERSON_ADDRESS = (By.CSS_SELECTOR, "#address2")
    COUNTRY = (By.CSS_SELECTOR, "#country")
    ZIPCODE = (By.CSS_SELECTOR, "#zipcode")
    PHONE_NUMBER = (By.CSS_SELECTOR, "#mobile_number")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[data-qa = 'create-account']")