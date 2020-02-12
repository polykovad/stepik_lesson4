from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.locators import MainPageLocators
from .pages.locators import BasePageLocators
from .pages.locators import LoginPageLocators
from .pages.basket_page import BasketPage
import pytest
import time

#@pytest.mark.parametrize("link", ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                                marks=pytest.mark.xfail),
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser): #использовать при использовавнии LINK_MAIN
#def test_guest_can_add_product_to_basket(browser, link):
    link = MainPageLocators.LINK_MAIN

    #открываем страницу
    page = ProductPage(browser, link)
    page.open()

    #проверка на правильность ссылки
    page.should_be_nice_link()

    #проверка на добавление в корзину
    page.should_add_product()

    #решаем пример
    page.solve_quiz_and_get_code()

    #проверяем правильность добавленной книги
    page.should_product_correct()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = MainPageLocators.LINK_MAIN

    # открываем страницу
    page = ProductPage(browser, link)
    page.open()

    # проверка на добавление в корзину
    page.should_add_product()

    #решаем пример
    page.solve_quiz_and_get_code()


    #проверяем, что нет сообщения об успехе с помощью
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = MainPageLocators.LINK_MAIN

    # открываем страницу
    page = ProductPage(browser, link)
    page.open()

    #проверяем, что нет сообщения об успехе с помощью
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = MainPageLocators.LINK_MAIN

    # открываем страницу
    page = ProductPage(browser, link)
    page.open()

    # проверка на добавление в корзину
    page.should_add_product()

    # решаем пример
    page.solve_quiz_and_get_code()

    #gроверяем, что нет сообщения об успехе
    page.should_not_be_success_message_disapeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = MainPageLocators.LINK_MAIN_PAGE

    # открываем страницу
    page = ProductPage(browser, link)
    page.open()

    page.go_to_basket()

    page = BasketPage(browser,link)
    page.should_be_empty_basket()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = MainPageLocators.LINK_MAIN

    # открываем страницу
    page = ProductPage(browser, link)
    page.open()

    page.go_to_basket()
    basket = BasketPage(browser, link)
    basket.should_be_empty_basket()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = MainPageLocators.LINK_MAIN
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(3)
    page.should_be_login_page
    time.sleep(3)


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = LoginPageLocators.LINK_LOGIN
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_register_form()
        page.should_be_add_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):

        #проверка сообщения
        link = MainPageLocators.LINK_MAIN

        # открываем страницу
        page = ProductPage(browser, link)
        page.open()

        # проверяем, что нет сообщения об успехе с помощью
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):

        #добавляем продукт в корзину
        link = MainPageLocators.LINK_MAIN

        # открываем страницу
        page = ProductPage(browser, link)
        page.open()

        # проверка на правильность ссылки
        page.should_be_nice_link()

        # проверка на добавление в корзину
        page.should_add_product()

        # решаем пример
        page.solve_quiz_and_get_code()

        # проверяем правильность добавленной книги
        page.should_product_correct()

        page.go_to_basket()

        basket = BasketPage(browser, link)
        basket.should_delete_product()

        time.sleep(1)
