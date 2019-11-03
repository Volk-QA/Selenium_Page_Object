from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
	
	def check_basket(self):
		self.should_not_be_product_in_basket()
		self.should_text_basket_empty()
	
	def should_not_be_product_in_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

	def should_text_basket_empty(self):
		basket_message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text
		assert len(basket_message) > 0, "Basket is not empty"