class BasePage():
	def __init__(self, browser, url):
		self.browser = browser
		self.ulr = url
	def open(self):
		self.browser.get(self.url)