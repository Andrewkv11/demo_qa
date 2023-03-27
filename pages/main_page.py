from .base_page import BasePage
from locators.locators import MainPageLocators
import allure


class MainPage(BasePage):

    def go_to_page(self, page):
        with allure.step(f'Go to page: {page}'):
            self.element_is_clickable(self.format_locator(MainPageLocators.MENU_CARD, page)).click()
