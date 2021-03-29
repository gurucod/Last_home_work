from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators, MainPageLocators
import math


class BasePage():
    """Базовый класс который поключает браузер и url. Так же добавляет методы open и
    is_element_present для перехода на страницу по url и ловит ошибки NoSuchElementException"""

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        """Переходим на страницу Авторизации/Регистрации"""
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_page(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        """Нажимает на кнопку 'Корзина' и переходим в корзину """
        link = self.browser.find_element(*MainPageLocators.BASKET_BUTTON)
        link.click()

    def is_element_present(self, how, what):
        """Метод BasePage. Метод is_element_present, в котором перехватываются исключения.
        В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать
        (строку-селектор)."""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

        return True

    def is_not_element_present(self, how, what, timeout=4):
        """Метод, который проверяет, что элемент не появляется на странице в течение заданного времени.
        is_not_element_present: упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        """Проверить, что какой-то элемент исчезает, используем явное ожидание вместе с функцией until_not.
        is_disappeared: будет ждать до тех пор, пока элемент не исчезнет. """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def solve_quiz_and_get_code(self):
        """Метод в тесте для получения проверочного кода"""
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")