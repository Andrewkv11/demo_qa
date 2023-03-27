from selenium.webdriver.common.by import By


class MainPageLocators:
    MENU_CARD = (By.XPATH, "//h5[text()='{}']//ancestor::div[contains(@class, 'top-card')]")


class ElementsPageLocators:
    ELEMENTS_CARD = (By.XPATH, "//span[text()='{}']//ancestor::li")


class CheckBoxPageLocators:
    EXPAND_BUTTON = (By.XPATH, "//span[text()='{}']//ancestor::li[1]/span/button")
    EXPAND_ITEMS = (By.XPATH, "//span[text()='{}']//ancestor::li[1]//ol")
    CHECKBOX_CHOICE = (By.XPATH, "//span[text()='{}']")
    CHECKED_ITEM = (By.XPATH, "//span[text()='{}']//ancestor::label//span[1]//*[name()='svg']")
    DISPLAY_RESULT = (By.XPATH, "//div[@id='result']//span")


class BasePageLocators:
    MAIN_HEADER = (By.XPATH, "//div[@class='main-header']")
