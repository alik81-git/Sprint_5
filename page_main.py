from page_base import BasePage
from locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def click_entry_button(self):
        self.click(MainPageLocators.ENTRY_BUTTON)

    def click_place_ad_button(self):
        self.click(MainPageLocators.PLACE_AD_BUTTON)

    def click_publish_ad_button(self):
        self.click(MainPageLocators.PUBLISH_AD_BUTTON)

    def click_logout_button(self):
        self.click(MainPageLocators.LOGOUT_BUTTON)

    def is_user_avatar_visible(self):
        return self.is_element_visible(MainPageLocators.USER_AVATAR)

    def is_user_name_visible(self):
        return self.is_element_visible(MainPageLocators.USER_NAME)

    def is_entry_button_visible(self):
        return self.is_element_visible(MainPageLocators.ENTRY_BUTTON)

    def get_user_name(self):
        return self.get_text(MainPageLocators.USER_NAME)

    def go_profile(self):
        self.click(MainPageLocators.GO_PROFILE)

    def search_item_name(self):
        return self.get_text(MainPageLocators.FIND_ITEM_NAME)

    def open(self):
        # Открыть главную страницу
        self.driver.get("https://qa-desk.stand.praktikum-services.ru/")
