from .base_page import BasePage
from .locators import MainPageLocators
from .locators import BasePageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        print(self.browser.find_element(*MainPageLocators.EMPTY_BASKET).text)
        assert (self.browser.find_element(*MainPageLocators.EMPTY_BASKET).text == "Your basket is empty. Continue shopping"), \
            "Basket is not empty"

    def should_delete_product(self):
        field = self.browser.find_element(*BasePageLocators.FIELD_NUM)
        field.clear()
        field.send_keys("0")
        button_update = self.browser.find_element(*BasePageLocators.UPDATE_BUTTON)
        button_update.click()