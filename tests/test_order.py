import pytest
import allure
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.title("Инициализация драйвера Firefox")
@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()

@allure.feature("Оформление заказа")
@allure.story("Позитивный сценарий с параметризацией")
@pytest.mark.parametrize("is_top_button, order_data", [
    (True, {
        "first_name": "Алексей",
        "last_name": "Смирнов",
        "address": "проспект Мира, д.12",
        "metro": "ВДНХ",
        "phone": "+79261234567",
        "date": "08.08.2025",
        "rent_duration": "трое суток",
        "color": "grey"
    }),
    (False, {
        "first_name": "Мария",
        "last_name": "Кузнецова",
        "address": "улица Тверская, д.7",
        "metro": "Пушкинская",
        "phone": "+79269876543",
        "date": "08.08.2025",
        "rent_duration": "сутки",
        "color": "black"
    }),
])
def test_successful_order(driver, is_top_button, order_data):
    home_page = MainPage(driver)
    home_page.open()
    home_page.close_cookie_banner()
    home_page.click_order_button(is_top=is_top_button)

    order_page = OrderPage(driver)
    order_page.fill_order_form(order_data)
    assert order_page.is_order_successful(), "Окно подтверждения заказа не появилось"
    success_text = order_page.wait.until(
    EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Заказ оформлен')]"))
)
    assert "Заказ оформлен" in success_text.text

@allure.feature("Навигация")
@allure.story("Переход по логотипу Самоката на главную страницу")
def test_scooter_logo_redirects_to_home(driver):
    home_page = MainPage(driver)
    home_page.open()
    home_page.close_cookie_banner()
    home_page.click_order_button(is_top=True)

    order_page = OrderPage(driver)
    home_url = home_page.base_url
    redirected_url = home_page.click_scooter_logo()
    assert redirected_url == home_url, f"Ожидался редирект на {home_url}, но был {redirected_url}"

@allure.feature("Навигация")
@allure.story("Переход по логотипу Яндекса на Дзен")
def test_yandex_logo_opens_dzen(driver):
    home_page = MainPage(driver)
    home_page.open()
    home_page.close_cookie_banner()
    home_page.click_order_button(is_top=True)

    order_page = OrderPage(driver)
    url = home_page.click_yandex_logo()
    assert "dzen.ru" in url, f"Ожидался переход на Дзен, но url: {url}"
