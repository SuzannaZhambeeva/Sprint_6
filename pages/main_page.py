from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.common.exceptions import ElementClickInterceptedException


class MainPage(BasePage):

    URL = "https://qa-scooter.praktikum-services.ru/"

    TOP_ORDER_BUTTON = MainPageLocators.TOP_ORDER_BUTTON
    BOTTOM_ORDER_BUTTON = MainPageLocators.BOTTOM_ORDER_BUTTON
    SCOOTER_LOGO = MainPageLocators.SCOOTER_LOGO
    YANDEX_LOGO = MainPageLocators.YANDEX_LOGO

    def open(self):
        super().open(self.URL)

    def click_faq_question(self, question_locator, answer_locator):
        self.scroll_to_element(question_locator)
        self.click_element(question_locator)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(answer_locator)
        )
        return self.find_element(answer_locator).text

    def click_order_button(self, is_top=True):
        button_locator = self.TOP_ORDER_BUTTON if is_top else self.BOTTOM_ORDER_BUTTON
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(button_locator))
        self.scroll_to_element(button_locator)
        element = self.find_element(button_locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)


    def click_scooter_logo(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.SCOOTER_LOGO)
        )
        self.click_element(self.SCOOTER_LOGO)
        return self.get_current_url()

    def click_yandex_logo(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.YANDEX_LOGO)
        )
        self.click_element(self.YANDEX_LOGO)

        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        new_window = [w for w in self.driver.window_handles if w != self.driver.current_window_handle][0]
        self.driver.switch_to.window(new_window)

        WebDriverWait(self.driver, 10).until(lambda d: d.current_url != "about:blank")

        return self.get_current_url()
    
    def click_faq_question_safe(self, question_locator, answer_locator):
        try:
            self.click_element(question_locator)
        except ElementClickInterceptedException:
            element = self.find_element(question_locator)
            self.driver.execute_script("arguments[0].click();", element)
        self.wait.until(EC.visibility_of_element_located(answer_locator))
        return self.find_element(answer_locator).text
