from page_base import BasePage
from locators import MainPageLocators

class MainPage(BasePage):
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