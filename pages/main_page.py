from .base_page import BasePage
from .locators import MainPageLocators
#import time


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        alert = self.browser.switch_to.alert
        alert.accept()
        #time.sleep(10)

    def should_be_login_link(self):
        """Проверка что присутствует кнопка аторизации/регистрации на странице"""
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"