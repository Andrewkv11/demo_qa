import allure

from pages.base_page import BasePage
from locators.locators import CheckBoxPageLocators


class CheckBoxPage(BasePage):

    def expand_folder(self, folder):
        with allure.step(f'Expand folder: {folder}'):
            self.element_is_clickable(self.format_locator(CheckBoxPageLocators.EXPAND_BUTTON, folder)).click()

    def click_checkbox(self, checkbox):
        with allure.step(f'Click checkbox: {checkbox}'):
            self.element_is_clickable(self.format_locator(CheckBoxPageLocators.CHECKBOX_CHOICE, checkbox)).click()

    def check_checkbox_choice(self, checkbox):
        with allure.step(f'Expand folder: {checkbox}'):
            checkbox_choice = self.element_is_visible(self.format_locator(CheckBoxPageLocators.CHECKED_ITEM, checkbox))
            return checkbox_choice.get_attribute('class') == 'rct-icon rct-icon-check'

    def parse_result(self):
        with allure.step('Parse result'):
            results = [result.text for result in self.elements_are_visible(CheckBoxPageLocators.DISPLAY_RESULT)]
            return results

    def check_expanding(self, folder):
        with allure.step(f'Check expanding folder: {folder}'):
            return self.element_is_visible(self.format_locator(CheckBoxPageLocators.EXPAND_ITEMS, folder))
