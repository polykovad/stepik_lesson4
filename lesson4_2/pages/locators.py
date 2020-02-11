from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    LINK_MAIN = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"

class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    LINK_LOGIN = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"