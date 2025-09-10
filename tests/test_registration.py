import pytest
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_main import MainPage
from page_registration import RegistrationPage
from helpers import generate_email, generate_password


# Новый пользователь по маске
class TestRegistrationByMask:
    @pytest.mark.positive
    def test_successful_registration(self, driver, wait):
        main_page = MainPage(driver, wait)
        registration_page = RegistrationPage(driver, wait)

        main_page.open()
        main_page.click_entry_button()

        email = generate_email()
        password = generate_password()

        registration_page.register_user(email, password)

        assert (
            main_page.is_user_avatar_visible()
        ), "User avatar is not visible after registration"  # проверка аватара
        assert (
            main_page.is_user_name_visible()
        ), "User name is not visible after registration"  # проверка имени


# Новый пользователь не по маске
class TestRegistrationBadMask:
    @pytest.mark.negative
    def test_registration_with_invalid_email(self, driver, wait):
        main_page = MainPage(driver, wait)
        registration_page = RegistrationPage(driver, wait)

        main_page.open()
        main_page.click_entry_button()
        registration_page.click_no_account_button()

        registration_page.input_email("invalid-email")
        registration_page.input_password("invalid-password")
        registration_page.input_submit_password("invalid-password")
        registration_page.click_create_account_button()

        assert (
            registration_page.is_email_field_highlighted()
        ), "Email field is not highlighted"  # проверка подсветки email
        assert (
            registration_page.is_password_field_highlighted()
        ), "Password field is not highlighted"  # проверка подсветки password
        assert (
            registration_page.is_submit_password_field_highlighted()
        ), "Submit password field is not highlighted"  # проверка подсветки submit password
        assert (
            registration_page.is_error_text_message_visible()
        ), "Error message is not visible for invalid email"  # проверка сообщения Ошибка


# Регистрация уже существующего пользователя
class TestExistUser:
    @pytest.mark.negative
    def test_registration_existing_user(self, driver, wait):
        main_page = MainPage(driver, wait)
        registration_page = RegistrationPage(driver, wait)

        main_page.open()
        main_page.click_entry_button()
        registration_page.click_no_account_button()

        registration_page.input_email("qa_python_25@mail.ru")
        registration_page.input_password("qa_python_25")
        registration_page.input_submit_password("qa_python_25")
        registration_page.click_create_account_button()

        assert (
            registration_page.is_email_field_highlighted()
        ), "Email field is not highlighted"  # проверка подсветки email
        assert (
            registration_page.is_password_field_highlighted()
        ), "Password field is not highlighted"  # проверка подсветки password
        assert (
            registration_page.is_submit_password_field_highlighted()
        ), "Submit password field is not highlighted"  # проверка подсветки submit password
        assert (
            registration_page.is_error_text_message_visible()
        ), "Error message is not visible for invalid email"  # проверка сообщения Ошибка
