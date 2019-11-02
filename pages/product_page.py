from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def add_to_basket(self):
		add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
		add_to_basket_button.click()
	def check_add_to_basket_true(self):
		price =                self.browser.find_element(*ProductPageLocators.ORIGINAL_PRICE).text
		price_message =        self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_BASKET).text
		product_name =         self.browser.find_element(*ProductPageLocators.ORIGINAL_NAME_PRODUCT).text
		product_name_message = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME_PRODUCT).text
		assert self.is_element_present(*ProductPageLocators.MESSAGE_IF_ADD_TO_BASKET), "Message HAS BEEN ADDED TO YOUR BASKET not presented"
		assert self.is_element_present(*ProductPageLocators.MESSAGE_PRICE_BASKET), "Message with price a basket not present"
		assert product_name == product_name_message, "Product name in basket not matches with choicible product"
		assert price == price_message, "Original price not matches with price in basket"