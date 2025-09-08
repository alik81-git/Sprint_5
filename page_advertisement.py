from page_base import BasePage
from locators import AdvertisementPageLocators
from selenium.webdriver.common.keys import Keys


class AdvertisementPage(BasePage):
    def get_modal_title(self):
        return self.find_elements(AdvertisementPageLocators.MODAL_TITLE)

    def input_title(self, title):
        self.input_text(AdvertisementPageLocators.TITLE_INPUT, title)

    def input_description(self, description):
        self.input_text(AdvertisementPageLocators.DESCRIPTION_INPUT, description)

    def input_price(self, price):
        self.input_text(AdvertisementPageLocators.PRICE_INPUT, price)

    def select_category(self, category):
        dropdown = self.find_element(AdvertisementPageLocators.CATEGORY_DROPDOWN)
        dropdown.send_keys(category)

    def select_city(self, city):
        dropdown = self.find_element(AdvertisementPageLocators.CITY_DROPDOWN)
        dropdown.send_keys(city)

    def select_condition(self, condition):
        conditions = self.find_elements(AdvertisementPageLocators.CONDITION_RADIO)
        for cond in conditions:
            if cond.get_attribute("value") == condition:
                cond.click()
                break

    def click_publish_button(self):
        self.click(AdvertisementPageLocators.PUBLISH_BUTTON)

    def is_advertisement_visible(self):
        return self.is_element_visible(AdvertisementPageLocators.ADVERTISEMENT_ITEM)
    
    def set_item_name(self):
        self.input_text(AdvertisementPageLocators.ITEM_NAME).send_keys('123')

    def create_advertisement(self, title, description, price, category, city, condition):
        self.input_title(title)
        self.input_description(description)
        self.input_price(price)
        self.select_category(category)
        self.select_city(city)
        self.select_condition(condition)
        self.click_publish_button()
