import pytest
from data import TestData
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


# инициализируем инстанс вебдрайвера
@pytest.fixture
def driver():
    chrome_options = Options()
    # Режим инкогнито, для отключения предупреждений об утечках
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(TestData.user_data()["base_url"])
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)
