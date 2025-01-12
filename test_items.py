import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


def test_exist_add_button_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.'
    browser.get(link)
    button_basket = WebDriverWait(browser,5).until(
        Ec.visibility_of_element_located((By.CSS_SELECTOR, '#add_to_basket_form > button'))
    )
    assert button_basket, 'Кнопка "Добавить в корзину" отсутствует'




