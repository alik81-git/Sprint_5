from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.base_url = "https://qa-desk.stand.praktikum-services.ru/"

    def open(self):
        self.driver.get(self.base_url)

    def find_element(self, locator, timeout=10):
        return self.wait.until(EC.presence_of_element_located(locator),
                              message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, timeout=10):
        return self.wait.until(EC.presence_of_all_elements_located(locator),
                              message=f"Can't find elements by locator {locator}")

    def click(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    def input_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, locator, timeout=10):
        try:
            print(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def get_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text