import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    # chrome_options.add_argument("--headless")  # Раскомментировать для CI/CD
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    yield driver

    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)


# Дополнительные фикстуры для часто используемых ожиданий
@pytest.fixture
def ec():
    #Фикстура для удобного доступа к expected_conditions
    return EC
