from selenium.webdriver.common.by import By


class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_MAIL = (By.CSS_SELECTOR, "input[name='login-username']" )
	LOGIN_PASS = (By.CSS_SELECTOR, "input[name='login-password']" )
	REG_MAIL = (By.CSS_SELECTOR, "input[name='registration-email']" )
	REG_PASS = (By.CSS_SELECTOR, "input[name='registration-password1']" )
	REG_CONFIRM_PASS = (By.CSS_SELECTOR, "input[name='registration-password2']" )

class ProductPageLocators():
	ADD_TO_BASKET = (By.CSS_SELECTOR, "form[id='add_to_basket_form']>button" )
	ORIGINAL_NAME_PRODUCT = (By.CSS_SELECTOR, "article[class='product_page'] h1" )
	ORIGINAL_PRICE = (By.CSS_SELECTOR, "article[class='product_page'] p[class='price_color']" )
	MESSAGE_IF_ADD_TO_BASKET = (By.CSS_SELECTOR, "div#messages div.alertinner:nth-child(2)" )
	MESSAGE_NAME_PRODUCT = (By.CSS_SELECTOR, "div#messages div.alertinner:nth-child(2)>strong" )
	MESSAGE_PRICE_BASKET = (By.CSS_SELECTOR, "div#messages div.alert-info>div.alertinner strong" )

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	BASKET_LINK = (By.CSS_SELECTOR,"div.basket-mini a" )
class BasketPageLocators():
	BASKET_EMPTY = (By.CSS_SELECTOR,"div#content_inner>p" )
	BASKET_ITEMS = (By.CSS_SELECTOR,"div.basket-items" )
