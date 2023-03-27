from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import BasePageLocators


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def go_to_element(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView;", element)

    def get_current_url(self):
        return self.driver.current_url

    def parse_header(self):
        return self.element_is_visible(BasePageLocators.MAIN_HEADER).text

    def format_locator(self, locator, param):
        return locator[0], locator[1].format(param)
