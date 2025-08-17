from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self, url=None):
        self.driver.get(url or self.base_url)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    def click_element(self, locator):
        element = self.scroll_to_element(locator)
        self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_current_url(self):
        return self.driver.current_url

    def close_cookie_banner(self):
        try:
            cookie_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except TimeoutException:
            pass
