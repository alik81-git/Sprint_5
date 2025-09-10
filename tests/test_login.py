import pytest
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_main import MainPage
from page_login import LoginPage


class TestUserLogin:
    @pytest.mark.positive
    def test_successful_login(self, driver, wait):
        main_page = MainPage(driver, wait)
        login_page = LoginPage(driver, wait)

        main_page.open()
        main_page.click_entry_button()  # Нажать кнопку «Вход и регистрация».
        login_page.login_user(
            "qa_python_25@mail.ru", "qa_python_25"
        )  # Заполнить все поля формы авторизации и нажать кнопку «Войти».

        assert (
            main_page.is_user_name_visible()
        ), "User name is not visible after login"  # Проверка отображения имени пользователя
        assert (
            main_page.is_user_avatar_visible()
        ), "User avatar is not visible after login"  # Проверка отображения аватара
        assert (
            main_page.get_current_url()
            == "https://qa-desk.stand.praktikum-services.ru/login"
        )  # Проверка перехода на главную страницу
