from .base_page import BasePage
from .locators import MainPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time

class ProductPage(BasePage):
    def should_be_nice_link(self):
        # реализуйте проверку на корректный url адрес
        s = self.browser.current_url
        print("actual link - " + s)
        time.sleep(1)

        print("Проверочный код - " + s[73:])
        assert s[73:] == MainPageLocators.CODE, "Url is not correct !"

        #print("Проверочный код - " + s[73:85])
        #assert s[73:85] == MainPageLocators.CODE, "Url is not correct !"

    def should_add_product(self):
        #нажать на кнопку "добавить в корзину"
        button_add = self.browser.find_element(*MainPageLocators.BUTTON_ADD)
        button_add.click()
        time.sleep(1)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            time.sleep(2)
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_not_be_success_message(self):
       assert self.is_not_element_present(*MainPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_disapeared(self):
       assert self.is_disappeared(*MainPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared, but should not be"

    def should_product_correct(self):
        #находим название книги и цену
        name_product = self.browser.find_element(*MainPageLocators.NAME_PRODUCT_OUR)
        name_product = name_product.text
        price_product = self.browser.find_element(*MainPageLocators.PRICE_PRODUCT_OUR)
        price_product = price_product.text
        #basket = self.browser.find_element(*MainPageLocators.BUTTON_BASKET)
        time.sleep(2)

        print("\nName book on the page - " + name_product)
        print("\nPrice book on the page - " + price_product)

        print("\nName book in basket - " + self.browser.find_element(*MainPageLocators.NAME_IN_ALERT).text)
        print("\nPrice book in basket - " + self.browser.find_element(*MainPageLocators.PRICE_IN_ALERT).text)

        assert (name_product == self.browser.find_element(*MainPageLocators.NAME_IN_ALERT).text
                and price_product == self.browser.find_element(*MainPageLocators.PRICE_IN_ALERT).text), "Not correct name and price in basket"

        print("\nBook " + name_product + " was added!")


