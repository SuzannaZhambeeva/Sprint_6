from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class MainPage:
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (By.CLASS_NAME, "Button_Button__ra12g")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    COOKIE_BUTTON = (By.CLASS_NAME, "App_CookieButton__3cvqF")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    def open(self):
        self.driver.get(self.base_url)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        ActionChains(self.driver).move_to_element(element).perform()
        element.click()

    def click_faq_question(self, question_locator, answer_locator):
        element = self.find_element(question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click_element(question_locator)
        return self.find_element(answer_locator).text

    def click_order_button(self, is_top=True):
        locator = self.ORDER_BUTTON_TOP if is_top else self.ORDER_BUTTON_BOTTOM
        self.click_element(locator)

    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)
        return self.get_current_url()

    def click_yandex_logo(self):
        original_window = self.driver.current_window_handle
        self.click_element(self.YANDEX_LOGO)

        self.wait.until(EC.number_of_windows_to_be(2))

        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        self.driver.switch_to.window(new_window)

        self.wait.until(lambda d: d.current_url != "about:blank")

        url = self.get_current_url()
        self.driver.close()
        self.driver.switch_to.window(original_window)
        return url


    def click_top_order_button(self):
        self.click_element(self.ORDER_BUTTON_TOP)

    def click_bottom_order_button(self):
        buttons = self.driver.find_elements(By.CLASS_NAME, "Button_Button__ra12g")
        if len(buttons) >= 2:
            button = buttons[1]
            self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
            ActionChains(self.driver).move_to_element(button).perform()
            self.wait.until(EC.element_to_be_clickable(button)).click()
        else:
            raise Exception("Кнопка внизу не найдена")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def close_cookie_banner(self):
        try:
            cookie_button = self.driver.find_element(*self.COOKIE_BUTTON)
            cookie_button.click()
        except:
            pass

    def get_current_url(self):
        return self.driver.current_url
