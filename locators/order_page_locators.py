from selenium.webdriver.common.by import By

class OrderPageLocators:
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = lambda metro: (By.XPATH, f"//button/div[text()='{metro}']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-arrow")
    RENT_OPTION = lambda duration: (By.XPATH, f"//div[text()='{duration}']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons__')]/button[normalize-space()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
