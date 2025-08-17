from selenium.webdriver.common.by import By


class FAQQuestionLocators:
    COST = (By.XPATH, "//*[@id='accordion__heading-0']")
    FEW_OBJECTS = (By.XPATH, "//*[@id='accordion__heading-1']")
    TIME_RENT = (By.XPATH, "//*[@id='accordion__heading-2']")
    TODAY_ORDER = (By.XPATH, "//*[@id='accordion__heading-3']")
    EXTENSION_OR_REFUND = (By.XPATH, "//*[@id='accordion__heading-4']")
    CHARGER_WITH_ORDER = (By.XPATH, "//*[@id='accordion__heading-5']")
    CANSEL_ORDER = (By.XPATH, "//*[@id='accordion__heading-6']")
    AREA_OF_ORDER = (By.XPATH, "//*[@id='accordion__heading-7']")
    
class FAQAnswerLocators:
    COST = (By.XPATH, "//*[@id='accordion__panel-0']/p")
    FEW_OBJECTS = (By.XPATH, "//*[@id='accordion__panel-1']/p")
    TIME_RENT = (By.XPATH, "//*[@id='accordion__panel-2']/p")
    TODAY_ORDER = (By.XPATH, "//*[@id='accordion__panel-3']/p")
    EXTENSION_OR_REFUND = (By.XPATH, "//*[@id='accordion__panel-4']/p")
    CHARGER_WITH_ORDER = (By.XPATH, "//*[@id='accordion__panel-5']/p")
    CANSEL_ORDER = (By.XPATH, "//*[@id='accordion__panel-6']/p")
    AREA_OF_ORDER = (By.XPATH, "//*[@id='accordion__panel-7']/p")