import allure
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.main_page import MainPage
from locators import FAQQuestionLocators, FAQAnswerLocators

@allure.feature("FAQ")
class TestFAQ:

    @allure.story("Сколько это стоит?")    
    def test_faq_questions_cost_question(self):
        main_page = MainPage(webdriver.Firefox())
        main_page.driver.get('https://qa-scooter.praktikum-services.ru/')
        expected_answer = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        answer = main_page.click_faq_question(FAQQuestionLocators.COST, FAQAnswerLocators.COST)
        assert answer == expected_answer, f"Ответ для вопроса не совпадает: ожидался {expected_answer}, получен {answer}"
        main_page.driver.quit() 

    @allure.story("Можно ли заказать несколько самокатов?")    
    def test_faq_questions_few_object_question(self):
        main_page = MainPage(webdriver.Firefox())
        main_page.driver.get('https://qa-scooter.praktikum-services.ru/')
        expected_answer = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        answer = main_page.click_faq_question(FAQQuestionLocators.FEW_OBJECTS, FAQAnswerLocators.FEW_OBJECTS)
        assert answer == expected_answer, f"Ответ для вопроса не совпадает: ожидался {expected_answer}, получен {answer}"
        main_page.driver.quit() 

    @allure.story("Когда начинается аренда?")    
    def test_faq_questions_time_rent_question(self):
        main_page = MainPage(webdriver.Firefox())
        main_page.driver.get('https://qa-scooter.praktikum-services.ru/')
        expected_answer = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        answer = main_page.click_faq_question(FAQQuestionLocators.TIME_RENT, FAQAnswerLocators.TIME_RENT)
        assert answer == expected_answer, f"Ответ для вопроса не совпадает: ожидался {expected_answer}, получен {answer}"
        main_page.driver.quit() 

    @allure.story("Можно ли заказать сегодня?")    
    def test_faq_questions_today_order_question(self):
        main_page = MainPage(webdriver.Firefox())
        main_page.driver.get('https://qa-scooter.praktikum-services.ru/')
        expected_answer = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        answer = main_page.click_faq_question(FAQQuestionLocators.TODAY_ORDER, FAQAnswerLocators.TODAY_ORDER)
        assert answer == expected_answer, f"Ответ для вопроса не совпадает: ожидался {expected_answer}, получен {answer}"
        main_page.driver.quit()   

    @allure.story("Можно ли продлить или отменить заказ?")    
    def test_faq_questions_extension_or_refund_question(self):
        main_page = MainPage(webdriver.Firefox())
        main_page.driver.get('https://qa-scooter.praktikum-services.ru/')
        expected_answer = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        answer = main_page.click_faq_question(FAQQuestionLocators.EXTENSION_OR_REFUND, FAQAnswerLocators.EXTENSION_OR_REFUND)
        assert answer == expected_answer, f"Ответ для вопроса не совпадает: ожидался {expected_answer}, получен {answer}"
        main_page.driver.quit()  

    @allure.story("Нужна ли зарядка?")    
    def test_faq_questions_charger_with_order_question(self):
        main_page = MainPage(webdriver.Firefox())
        main_page.driver.get('https://qa-scooter.praktikum-services.ru/')
        expected_answer = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        answer = main_page.click_faq_question(FAQQuestionLocators.CHARGER_WITH_ORDER, FAQAnswerLocators.CHARGER_WITH_ORDER)
        assert answer == expected_answer, f"Ответ для вопроса не совпадает: ожидался {expected_answer}, получен {answer}"
        main_page.driver.quit()  

    @allure.story("Можно ли отменить заказ?")    
    def test_faq_questions_cansel_order_question(self):
        main_page = MainPage(webdriver.Firefox())
        main_page.driver.get('https://qa-scooter.praktikum-services.ru/')
        expected_answer = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        answer = main_page.click_faq_question(FAQQuestionLocators.CANSEL_ORDER, FAQAnswerLocators.CANSEL_ORDER)
        assert answer == expected_answer, f"Ответ для вопроса не совпадает: ожидался {expected_answer}, получен {answer}"
        main_page.driver.quit()   

    @allure.story("Где работает доставка?")    
    def test_faq_questions_area_of_order_question(self):
        main_page = MainPage(webdriver.Firefox())
        main_page.driver.get('https://qa-scooter.praktikum-services.ru/')
        expected_answer = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        answer = main_page.click_faq_question(FAQQuestionLocators.AREA_OF_ORDER, FAQAnswerLocators.AREA_OF_ORDER)
        assert answer == expected_answer, f"Ответ для вопроса не совпадает: ожидался {expected_answer}, получен {answer}"
        main_page.driver.quit()   
        