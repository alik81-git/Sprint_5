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
        self.input_text(AdvertisementPageLocators.ITEM_NAME, "New item Name")

    def set_item_description(self):
        self.input_text(
            AdvertisementPageLocators.ITEM_DESCRIPTION, "New item Description"
        )

    def set_item_price(self):
        self.input_text(AdvertisementPageLocators.ITEM_PRICE, int(100))

    def set_item_radio_new(self):
        self.click(AdvertisementPageLocators.ITEM_RADIO_NEW)

    def set_item_radio_used(self):
        self.click(AdvertisementPageLocators.ITEM_RADIO_USED)

    def set_item_city_dropdown(self):
        self.click(AdvertisementPageLocators.ITEM_CITY_DROPDOWN)

    def set_item_lastcity(self):
        self.click(AdvertisementPageLocators.ITEM_LAST_CITY)

    def set_item_category_dropdown(self):
        self.click(AdvertisementPageLocators.ITEM_CATEGORY_DROPDOWN)

    def set_item_lastcategory(self):
        self.click(AdvertisementPageLocators.ITEM_LAST_CATEGORY)
