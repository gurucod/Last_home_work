from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        """Тут вызываются методы проверки пристутсвия элементов на странице"""
        self.should_be_login_url()
        self.should_be_button_basket()
        self.should_be_book_name_equal()
        self.should_be_price_basket_equal_book_price()

    def add_to_basket(self):
        """Нажатие на кнопку Добавление в корзину"""
        button_link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_link.click()

    def should_be_login_url(self):
        """Проверка что мы находимся на нужной странице"""
        assert "/catalogue/coders-at-work_207/" in self.url, "Проверьте URL, ОР: /coders-at-work_207/"

    def should_be_button_basket(self):
        """Проверка что кнопка добавления в корзину найдена"""
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Кнопка добавления в " \
                                                                                   "корзину не найдена на странице"

    def should_be_price_basket_equal_book_price(self):
        """Проверяется что стоимость корзины совпадает с ценой товара."""
        book_price = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_IN_PAGE).text
        book_price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_IN_BASKET).text
        assert book_price == book_price_basket, "Цена корзины не совпала с ценой товара"

    def should_be_book_name_equal(self):
        """Проверка того что название товара в сообщении совпадает с тем товаром, который был действительно добавлен."""
        book_name = self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_PAGE).text
        book_name_in_basket = self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_BASKET).text
        assert book_name == book_name_in_basket, "Название товара не совпало с добавленным в корзину товаром"

    def should_not_be_success_message(self):
        """Проверка того что на странице нет сообщения об успешном добавлении в корзину на данный момент"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успешном добавлении отображено,его не должно быть"

    def should_dissapear_of_success_message(self):
        """Проверка что элемент пропадает со страницы"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успешном добавлении не пропало в течении заданного периода"
