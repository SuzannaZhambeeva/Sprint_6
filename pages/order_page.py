import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Заполняем форму заказа")
    def fill_order_form(self, data):
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Имя']").send_keys(data["first_name"])
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Фамилия']").send_keys(data["last_name"])
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']").send_keys(data["address"])

        self.driver.find_element(By.XPATH, "//input[@placeholder='* Станция метро']").click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//button/div[text()='{data['metro']}']"))).click()

        self.driver.find_element(By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']").send_keys(data["phone"])
        self.driver.find_element(By.XPATH, "//button[text()='Далее']").click()

        date_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='* Когда привезти самокат']")))
        date_input.clear()
        date_input.send_keys(data["date"])
        date_input.send_keys(Keys.ENTER)

        self.driver.find_element(By.CLASS_NAME, "Dropdown-arrow").click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{data['rent_duration']}']"))).click()

        if data["color"] == "black":
            self.driver.find_element(By.ID, "black").click()
        elif data["color"] == "grey":
            self.driver.find_element(By.ID, "grey").click()

        order_button = self.wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//div[contains(@class, 'Order_Buttons__')]/button[normalize-space()='Заказать']"
    )))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_button)
        order_button.click()

        confirm_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Да']"))
        )
        confirm_button.click()

    def is_order_successful(self):
        try:
            self.wait.until(EC.visibility_of_element_located((
                By.XPATH,
                "//button[text()='Посмотреть статус']"
            )))
            return True
        except:
            return False

