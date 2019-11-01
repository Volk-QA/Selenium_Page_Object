from selenium.webdriver.common.by import By


class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_MAIL = (By.CSS_SELECTOR, "input[name='login-username']" )
	LOGIN_PASS = (By.CSS_SELECTOR, "input[name='login-password']" )
	REG_MAIL = (By.CSS_SELECTOR, "input[name='registration-email']" )
	REG_PASS = (By.CSS_SELECTOR, "input[name='registration-password1']" )
	REG_CONFIRM_PASS = (By.CSS_SELECTOR, "input[name='registration-password2']" )
