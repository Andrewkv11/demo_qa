from pages.base_page import BasePage
from locators.locators import ElementsPageLocators
import allure


class ElementsPage(BasePage):

    def go_to_page(self, page):
        with allure.step(f'Go to page {page}'):
            self.element_is_clickable(self.format_locator(ElementsPageLocators.ELEMENTS_CARD, page)).click()
