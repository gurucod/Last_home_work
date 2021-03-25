from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    FORM_LOGIN_ID = (By.CSS_SELECTOR, "#login_form")
    FORM_REGISTER_ID = (By.CSS_SELECTOR, "#register_form")

    # REGISTR_MAIL_LINK = (By.CSS_SELECTOR, "#id_registration-email")
    # REGISTR_PASS_LINK = (By.CSS_SELECTOR, "id_registration-password1")
    # REGISTR_PASS_CONF = (By.CSS_SELECTOR, "id_registration-password2")
    #
    # AUTH_MAIL_LINK = (By.CSS_SELECTOR, "id_login-username")
    # AUTH_PASS_LINK = (By.CSS_SELECTOR, "id_login-password")
