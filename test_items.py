import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


def test_exist_add_button_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.'
    browser.get(link)
    button_basket = browser.find_elements(By.CSS_SELECTOR, '#add_to_basket_form > button')
    assert len(button_basket) > 0, "Кнопка 'Добавить в корзину' не найдена на странице"




# Метод find_elementS позволяет на вернуть список всех элементов, подходящих под селектор.
# Логично предположить, что если на странице будет найден один элемент (кнопка),
# то длина списка будет отлична от нуля, поэтому в assert лучше задать проверку на длину списка
# find_elements возвращает список. Если элемент не найден, длина списка будет равна нулю.
# Проверка len(button_basket) > 0 гарантирует, что хотя бы один элемент найден.
# метод find_elements не выбрасывает исключение, если элементы не найдены.
# Он всегда возвращает пустой список []. Это ключевое отличие от метода find_element,
# который в случае отсутствия элемента вызывает исключение NoSuchElementException
# Использование find_elements с проверкой длины делает код устойчивее к отсутствию элемента
# и позволяет избежать непредвиденных остановок программы без дополнительного try-except.







