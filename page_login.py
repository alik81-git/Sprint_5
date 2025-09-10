from page_base import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def input_email(self, email):
        self.input_text(LoginPageLocators.EMAIL_INPUT, email)

    def input_password(self, password):
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def login_user(self, email, password):
        self.input_email(email)
        self.input_password(password)
        self.click_login_button()
