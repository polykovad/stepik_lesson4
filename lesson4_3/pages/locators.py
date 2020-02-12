from selenium.webdriver.common.by import By

class MainPageLocators():
    #ссылки
    #LINK_MAIN = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    LINK_MAIN = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #LINK_MAIN = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    LINK_MAIN_PAGE = "http://selenium1py.pythonanywhere.com/"

    #проверки
    CODE = "?promo=newYear2019"
    #CODE = "?promo=offer"

    #кнопка добавления в корзину
    BUTTON_ADD = (By.CSS_SELECTOR, "button.btn.btn.btn-lg.btn-primary")

    #название продукта на странице
    NAME_PRODUCT_OUR = (By.CSS_SELECTOR, 'h1:nth-child(1)')
    PRICE_PRODUCT_OUR = (By.XPATH, "//div[@class='col-sm-6 product_main']//p[@class='price_color']")

    #кнопка перехода в корзину
    BUTTON_BASKET = (By.XPATH, "//a[@class='btn btn-default']")

    #при переходе в корзину
    NAME_PRODUCT_BASKET = (By.XPATH, '//*[@id="basket_formset"]/div/div/div[2]/h3/a')
    PRICE_PRODUCT_BASKET = (By.XPATH, '//*[@id="basket_totals"]/table/tbody/tr[10]/td/h3')

    #на странице книги
    NAME_IN_ALERT = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRICE_IN_ALERT = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')

    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')

    EMPTY_BASKET = (By.XPATH, '//*[@id="content_inner"]')


class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    LINK_LOGIN = "http://selenium1py.pythonanywhere.com/accounts/login/"
    REG_BUTTON = (By.XPATH, "//button[@name='registration_submit']")
    LOGIN_BUTTON = (By.XPATH, "//button[@name='login_submit']")
    USERNAME = "mail_dasha@mail.com"
    PASSWORD = "pp012qq976"
    CLONE_PASSW = "pp012qq976"

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

    FIELD_NUM = (By.XPATH, "//input[@id='id_form-0-quantity']")

    UPDATE_BUTTON = (By.XPATH, "//span[@class='input-group-btn']//button[@class='btn btn-default']")