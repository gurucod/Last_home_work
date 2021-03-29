from .pages.product_page import ProductPage
from .pages.basked_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

link_product = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
link_Reg = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
promo_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, link_Reg)
        login_page.open()
        login_page.should_be_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = "stud1stud1"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, promo_link)
        page.open()
        page.should_be_button_basket()
        page.add_to_basket()
        time.sleep(1)
        page.solve_quiz_and_get_code()
        time.sleep(1)
        page.should_be_book_name_equal()
        page.should_be_price_basket_equal_book_price()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, promo_link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.parametrize('promo_code', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='Забагованный тест'))
                                        for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_code):
    url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_code}"
    page = ProductPage(browser, url)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.solve_quiz_and_get_code()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.verify_basket_is_empty()
    basket_page.should_be_message_basket_empty()


def test_guest_can_go_to_login_page_from_product_page(browser):
    """Гость может перейти на страницу авторизации из страницы продукта"""
    page = ProductPage(browser, link_product)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link_on_product_page(browser):
    """Кнопка авторизации видна со страницы продукта"""
    page = ProductPage(browser, link_product)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail(reason="тут текст причины метки")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, promo_link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, promo_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, promo_link)
    page.open()
    page.add_to_basket()
    page.should_dissapear_of_success_message()



