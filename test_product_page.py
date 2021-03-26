from .pages.product_page import ProductPage
import pytest
import time


@pytest.mark.parametrize('promo_code', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='Забагованный тест'))
                                        for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_code):
    url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_code}"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_page()
    #time.sleep(2)
