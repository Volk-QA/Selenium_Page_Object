from time import sleep
link ='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_cart_button(browser):
    browser.get(link)
    sleep(30)
    add_to_cart = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert add_to_cart, 'Кнопка добавления в корзину отсутствует'