from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    FORM_LOGIN_ID = (By.CSS_SELECTOR, "#login_form")
    FORM_REGISTER_ID = (By.CSS_SELECTOR, "#register_form")

