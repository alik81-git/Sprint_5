import pytest
import os, sys
curr_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(curr_dir)
sys.path.append(curr_dir)

from page_main import MainPage
from page_registration import RegistrationPage
from helpers import generate_email, generate_password

#Новый пользователь, проверка аватара
class TestRegistrationAvatar:
    @pytest.mark.positive
    def test_successful_registration(self, driver, wait):
        main_page = MainPage(driver, wait)
        registration_page = RegistrationPage(driver, wait)
        
        main_page.open()
        main_page.click_entry_button()
        
        email = generate_email()
        password = generate_password()
        
        registration_page.register_user(email, password)
        
        assert main_page.is_user_avatar_visible(), "User avatar is not visible after registration"

#Новый пользователь, проверка имени
class TestRegistrationUserName:
    @pytest.mark.positive
    def test_successful_registration(self, driver, wait):
        main_page = MainPage(driver, wait)
        registration_page = RegistrationPage(driver, wait)
        
        main_page.open()
        main_page.click_entry_button()
        
        email = generate_email()
        password = generate_password()
        
        registration_page.register_user(email, password)
        
        assert main_page.is_user_name_visible(), "User name is not visible after registration"

#Новый пользователь не по маске, проверка подсветки email
class TestRegistrationBadEmailRedError:
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
        
        assert registration_page.is_email_field_highlighted(), "Email field is not highlighted"

#Новый пользователь не по маске, проверка подсветки password
class TestRegistrationBadPasswordRedError:
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
        
        assert registration_page.is_password_field_highlighted(), "Password field is not highlighted"

#Новый пользователь не по маске, проверка подсветки submit password
class TestRegistrationBadSubmitPasswordRedError:
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
        
        assert registration_page.is_submit_password_field_highlighted(), "Submit password field is not highlighted"

#Новый пользователь не по маске, проверка сообщения Ошибка
class TestRegistrationBadEmailErrorRedMessage:
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
        
        assert registration_page.is_error_text_message_visible(), "Error message is not visible for invalid email"

#Регистрация уже существующего пользователя, проверка подсветки email
class TestExistUserBadEmailRedError:         
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
        
        assert registration_page.is_email_field_highlighted(), "Email field is not highlighted"

#Регистрация уже существующего пользователя, проверка подсветки password
class TestExistUserBadPasswordRedError:
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
        
        assert registration_page.is_password_field_highlighted(), "Password field is not highlighted"

#Регистрация уже существующего пользователя, проверка подсветки submit password
class TestExistUserBadSubmitPasswordRedError:
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
        
        assert registration_page.is_submit_password_field_highlighted(), "Submit password field is not highlighted"

#Регистрация уже существующего пользователя, проверка сообщения Ошибка
class TestExistUserBadEmailErrorRedMessage:
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
        
        assert registration_page.is_error_text_message_visible(), "Error message is not visible for invalid email"