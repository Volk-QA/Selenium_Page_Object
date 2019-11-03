from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        cur_url = self.browser.current_url
        assert "login" in cur_url, "Link broken"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_MAIL), "Login mail is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS), "Login pass is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_MAIL), "Reg mail is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS), "Reg pass is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_CONFIRM_PASS), "Reg pass confirm is not presented"
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_MAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_CONFIRM_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_CONFIRM_BUTTON).click()
        assert self.is_element_present(*LoginPageLocators.MESSAGE_CONFIRM_REG), "Registration failed"

