import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import allure
import pytest
import time
from selenium import webdriver
from locators.faq_locators import FAQQuestionLocators, FAQAnswerLocators
from pages.main_page import MainPage


@pytest.fixture(autouse=True)
def pause_between_tests():
    yield
    time.sleep(0.5)


@pytest.fixture(scope="class")
def main_page(request):
    driver = webdriver.Firefox()
    page = MainPage(driver)
    page.open()
    page.close_cookie_banner()
    request.cls.main_page = page
    yield
    driver.quit()


@allure.feature("FAQ")
@pytest.mark.usefixtures("main_page")
class TestFAQ:

    faq_data = [
        {"q": FAQQuestionLocators.COST,
         "a": FAQAnswerLocators.COST,
         "text": "Сутки — 400 рублей. Оплата курьеру — наличными или картой."},

        {"q": FAQQuestionLocators.FEW_OBJECTS,
         "a": FAQAnswerLocators.FEW_OBJECTS,
         "text": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."},

        {"q": FAQQuestionLocators.TIME_RENT,
         "a": FAQAnswerLocators.TIME_RENT,
         "text": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."},

        {"q": FAQQuestionLocators.TODAY_ORDER,
         "a": FAQAnswerLocators.TODAY_ORDER,
         "text": "Только начиная с завтрашнего дня. Но скоро станем расторопнее."},

        {"q": FAQQuestionLocators.EXTENSION_OR_REFUND,
         "a": FAQAnswerLocators.EXTENSION_OR_REFUND,
         "text": "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."},

        {"q": FAQQuestionLocators.CHARGER_WITH_ORDER,
         "a": FAQAnswerLocators.CHARGER_WITH_ORDER,
         "text": "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."},

        {"q": FAQQuestionLocators.CANSEL_ORDER,
         "a": FAQAnswerLocators.CANSEL_ORDER,
         "text": "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."},

        {"q": FAQQuestionLocators.AREA_OF_ORDER,
         "a": FAQAnswerLocators.AREA_OF_ORDER,
         "text": "Да, обязательно. Всем самокатов! И Москве, и Московской области."},
    ]

    @pytest.mark.parametrize("data", faq_data)
    def test_faq_questions(self, data):
        answer = self.main_page.click_faq_question_safe(data["q"], data["a"])
        assert answer == data["text"], (
            f"Ответ для вопроса не совпадает: ожидался '{data['text']}', получен '{answer}'"
        )
