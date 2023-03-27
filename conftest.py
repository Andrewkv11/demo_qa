import os
from selenium import webdriver
import pytest
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def driver(request):
    driver = None
    if request.param == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif request.param == 'firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    else:
        pytest.skip("Unsupported browser")
    driver.maximize_window()
    yield driver
    if os.path.exists("geckodriver.log"):
        os.remove("geckodriver.log")
    driver.quit()


