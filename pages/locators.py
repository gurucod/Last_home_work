from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    FORM_LOGIN_ID = (By.CSS_SELECTOR, "#login_form")
    FORM_REGISTER_ID = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRICE_BOOK_IN_PAGE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    PRICE_BOOK_IN_BASKET = (By.CSS_SELECTOR, "div#messages div:nth-child(3) div.alertinner strong")
    NAME_BOOK_IN_PAGE = (By.CSS_SELECTOR, "div.product_main h1")
    NAME_BOOK_IN_BASKET = (By.CSS_SELECTOR, "div#messages div:nth-child(1) strong")
    MASSAGE_SUCCESSFUL_ADD = (By.CSS_SELECTOR, "div#messages div:nth-child(1) div.alertinner")
