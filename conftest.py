import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

capabilities = {
	"browserName": "chrome",
	"version": "78.0",
	"enableVNC": True,
	"enableVideo": True
}


def pytest_addoption(parser):
	parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope='function')
def browser(request):
	lang = request.config.getoption('language')
	options = Options()
	options.add_experimental_option('prefs', {'intl.accept_languages': lang})
	print('\nstart Chrome browser...')
    # browser = webdriver.Chrome(options=options)
	browser = webdriver.Remote(
	command_executor="http://localhost:4444/wd/hub",
	desired_capabilities=capabilities,
	options=options
	)
	yield browser
	print('\nquit Chrome browser...')
	browser.quit()
#