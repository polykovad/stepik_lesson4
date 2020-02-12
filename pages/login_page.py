from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
from .locators import MainPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        s = self.browser.current_url
        assert s.find("/login"), "Url is nor correct !"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert (self.is_element_present(*LoginPageLocators.LOGIN_USERNAME)
                and self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD)), "Error in login field"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert (self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL)
                and self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWD1)
                and self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWD2)), "Error in registration field"

    def should_be_add_new_user(self):
        email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        generate_email = str(time.time()) + "@fakemail.org"
        email.send_keys(generate_email)
        pass1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWD1)
        pass1.send_keys(LoginPageLocators.CLONE_PASSW)
        pass2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWD2)
        pass2.send_keys(LoginPageLocators.CLONE_PASSW)
        button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        button.click()

    def should_be_login_user(self):
        email = self.browser.find_element(*LoginPageLocators.LOGIN_USERNAME)
        email.send_keys(LoginPageLocators.USERNAME)
        passwd = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        passwd.send_keys(LoginPageLocators.PASSWORD)
        button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        button.click()