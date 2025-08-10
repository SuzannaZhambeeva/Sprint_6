import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators as Locators
from pages.base_page import BasePage

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Заполняем форму заказа")
    def fill_order_form(self, data):
        self.click_element(Locators.FIRST_NAME_INPUT)
        self.find_element(Locators.FIRST_NAME_INPUT).send_keys(data["first_name"])

        self.click_element(Locators.LAST_NAME_INPUT)
        self.find_element(Locators.LAST_NAME_INPUT).send_keys(data["last_name"])

        self.click_element(Locators.ADDRESS_INPUT)
        self.find_element(Locators.ADDRESS_INPUT).send_keys(data["address"])

        self.click_element(Locators.METRO_INPUT)
        self.wait.until(EC.element_to_be_clickable(Locators.METRO_OPTION(data['metro']))).click()

        self.click_element(Locators.PHONE_INPUT)
        self.find_element(Locators.PHONE_INPUT).send_keys(data["phone"])

        self.click_element(Locators.NEXT_BUTTON)

        date_input = self.wait.until(EC.visibility_of_element_located(Locators.DATE_INPUT))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", date_input)
        date_input.clear()
        date_input.send_keys(data["date"])
        date_input.send_keys(Keys.ENTER)

        self.click_element(Locators.RENT_DROPDOWN)
        self.wait.until(EC.element_to_be_clickable(Locators.RENT_OPTION(data['rent_duration']))).click()

        if data["color"] == "black":
            self.click_element(Locators.COLOR_BLACK)
        elif data["color"] == "grey":
            self.click_element(Locators.COLOR_GREY)

        order_button = self.wait.until(EC.element_to_be_clickable(Locators.ORDER_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_button)
        order_button.click()

        confirm_button = self.wait.until(EC.element_to_be_clickable(Locators.CONFIRM_BUTTON))
        confirm_button.click()

    def is_order_successful(self):
        try:
            self.wait.until(EC.visibility_of_element_located(Locators.STATUS_BUTTON))
            return True
        except:
            return False
