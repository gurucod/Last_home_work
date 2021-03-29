from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group a")


class LoginPageLocators():
    FORM_LOGIN_ID = (By.CSS_SELECTOR, "#login_form")
    FORM_REGISTER_ID = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRICE_BOOK_IN_PAGE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    PRICE_BOOK_IN_BASKET = (By.CSS_SELECTOR, "div#messages div:nth-child(3) div.alertinner strong")
    NAME_BOOK_IN_PAGE = (By.CSS_SELECTOR, "div.product_main h1")
    NAME_BOOK_IN_BASKET = (By.CSS_SELECTOR, "div#messages div:nth-child(1) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1)")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators():
    MESSAGE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "div#content_inner >p")
    ITEM_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")