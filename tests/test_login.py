import pytest
import os, sys
curr_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(curr_dir)
sys.path.append(curr_dir)

from page_main import MainPage
from page_login import LoginPage

#Проверка отображения имени пользователя
class TestUserName:
    @pytest.mark.positive
    def test_successful_login(self, driver, wait):
        main_page = MainPage(driver, wait)
        login_page = LoginPage(driver, wait)
        
        main_page.open()
        main_page.click_entry_button() #Нажать кнопку «Вход и регистрация».
        login_page.login_user("qa_python_25@mail.ru", "qa_python_25") #Заполнить все поля формы авторизации и нажать кнопку «Войти».
                
        assert main_page.is_user_name_visible(), "User name is not visible after login"

#Проверка отображения аватара
class TestAvatar:
    @pytest.mark.positive
    def test_successful_login(self, driver, wait):
        main_page = MainPage(driver, wait)
        login_page = LoginPage(driver, wait)
        
        main_page.open()
        main_page.click_entry_button() #Нажать кнопку «Вход и регистрация».
        login_page.login_user("qa_python_25@mail.ru", "qa_python_25") #Заполнить все поля формы авторизации и нажать кнопку «Войти».
                
        assert main_page.is_user_avatar_visible(), "User avatar is not visible after login"

#Проверка перехода на главную страницу
class TestMainPage:
    @pytest.mark.positive
    def test_successful_login(self, driver, wait):
        main_page = MainPage(driver, wait)
        login_page = LoginPage(driver, wait)
        
        main_page.open()
        main_page.click_entry_button() #Нажать кнопку «Вход и регистрация».
        login_page.login_user("qa_python_25@mail.ru", "qa_python_25") #Заполнить все поля формы авторизации и нажать кнопку «Войти».
                
        assert driver.current_url == "https://qa-desk.stand.praktikum-services.ru/login"