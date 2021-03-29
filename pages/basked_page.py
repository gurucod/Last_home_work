from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_basket_empty(self):
        """Проверка что есть сообщение о том что корзина пуста"""
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), "Сообщение о том что корзина" \
                                                                                     " пустая отсутсвует"

    def verify_basket_is_empty(self):
        """Проверяем что в корзине нет товаров"""
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET), "Корзина не пустая"
