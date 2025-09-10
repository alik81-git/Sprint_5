import pytest
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_main import MainPage
from page_login import LoginPage


class TestUserLogout:
    @pytest.mark.positive
    def test_successful_login(self, driver, wait):
        main_page = MainPage(driver, wait)
        login_page = LoginPage(driver, wait)

        main_page.open()
        main_page.click_entry_button()  # Нажать кнопку «Вход и регистрация».
        login_page.login_user(
            "qa_python_25@mail.ru", "qa_python_25"
        )  # Заполнить все поля формы авторизации и нажать кнопку «Войти».
        main_page.click_logout_button()  # Разлогиниваемся

        assert (
            main_page.is_user_name_visible()
        ), "User name is visible after logout"  # Проверка отображения имени пользователя
        assert (
            main_page.is_user_avatar_visible()
        ), "User avatar is visible after logout"  # Проверка отображения аватара
        assert (
            main_page.is_entry_button_visible()
        ), "Entry button is not visible after logout"  # Проверка отображения кнопки «Вход и регистрация»
