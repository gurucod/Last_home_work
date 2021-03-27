from .pages.product_page import ProductPage
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"


# @pytest.mark.parametrize('promo_code', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='Забагованный тест'))
#                                         for i in range(10)])
# def test_guest_can_add_product_to_basket(browser, promo_code):
#     url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_code}"
#     page = ProductPage(browser, url)
#     page.open()
#     page.should_be_product_page()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     #time.sleep(2)

def test_guest_should_see_login_link_on_product_page(browser):
    """Кнопка авторизации видна со страницы продукта"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_page()


def test_guest_can_go_to_login_page_from_product_page(browser):
    """Гость может перейти на страницу авторизации из страницы продукта"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.xfail(reason="тут текст причины метки")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_dissapear_of_success_message()
