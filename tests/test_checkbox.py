import pytest
from pages.main_page import MainPage
from pages.elements_page import ElementsPage
from constants import BASE_URL, ELEMENTS_URL, ELEMENTS_PAGE, CHECKBOX_URL, CHECKBOX_PAGE
from pages.checkbox_page import CheckBoxPage
import allure


@allure.feature("Checkbox")
class TestCheckbox:

    @allure.title("Test Checkbox")
    @pytest.mark.parametrize('driver', ["chrome", "firefox"], indirect=True)
    def test_check_box(self, driver):
        main_page = MainPage(driver, BASE_URL)
        main_page.open()
        main_page.go_to_page(ELEMENTS_PAGE)

        elements_page = ElementsPage(driver, driver.current_url)
        current_url = elements_page.get_current_url()
        assert current_url == ELEMENTS_URL, f'Not correct page opened, current: {current_url}, expected: {ELEMENTS_URL}'
        main_header = elements_page.parse_header()
        assert main_header == ELEMENTS_PAGE, f'Not correct main header, current: {main_header}, ' \
                                             f'expected: {ELEMENTS_PAGE}'
        elements_page.go_to_page(CHECKBOX_PAGE)

        checkbox_page = CheckBoxPage(driver, driver.current_url)
        current_url = checkbox_page.get_current_url()
        assert current_url == CHECKBOX_URL, f'Not correct page opened, current: {current_url}, expected: {CHECKBOX_URL}'
        main_header = checkbox_page.parse_header()
        assert main_header == CHECKBOX_PAGE, f'Not correct main header, current: {main_header},' \
                                             f' expected: {CHECKBOX_PAGE}'

        checkbox_page.expand_folder('Home')
        assert checkbox_page.check_expanding('Home'), 'Wrong expanding'
        checkbox_page.expand_folder('Downloads')
        assert checkbox_page.check_expanding('Downloads'), 'Wrong expanding'
        checkbox_page.click_checkbox('Word File.doc')
        assert checkbox_page.check_checkbox_choice('Word File.doc'), 'Checkbox is not checked'
        results = checkbox_page.parse_result()
        assert results == ['You have selected :', 'wordFile'], 'Wrong checkbox selection result'
