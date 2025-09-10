from page_base import BasePage
from locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    def click_no_account_button(self):
        self.click(RegistrationPageLocators.NO_ACCOUNT_BUTTON)

    def input_email(self, email):
        self.input_text(RegistrationPageLocators.EMAIL_INPUT, email)

    def input_password(self, password):
        self.input_text(RegistrationPageLocators.PASSWORD_INPUT, password)

    def input_submit_password(self, password):
        self.input_text(RegistrationPageLocators.SUBMIT_PASSWORD_INPUT, password)

    def click_create_account_button(self):
        self.click(RegistrationPageLocators.CREATE_ACCOUNT_BUTTON)

    def is_error_text_message_visible(self):
        return self.is_element_visible(RegistrationPageLocators.ERROR_TEXT_FIELD)

    def is_email_field_highlighted(self):
        return self.find_elements(RegistrationPageLocators.ERROR_EMAIL)

    def is_password_field_highlighted(self):
        return self.find_elements(RegistrationPageLocators.ERROR_PASSWORD)

    def is_submit_password_field_highlighted(self):
        return self.find_elements(RegistrationPageLocators.ERROR_SUBMIT_PASSWORD)

    def register_user(self, email, password):
        self.click_no_account_button()
        self.input_email(email)
        self.input_password(password)
        self.input_submit_password(password)
        self.click_create_account_button()
