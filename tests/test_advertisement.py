import pytest
import os, sys
import time
curr_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(curr_dir)
sys.path.append(curr_dir)

from page_main import MainPage
from page_login import LoginPage
from page_advertisement import AdvertisementPage


#Создание объявления неавторизованным пользователем
class TestAdvertisementNegative:
    @pytest.mark.negative
    def test_create_advertisement_unauthorized(self, driver, wait):
        main_page = MainPage(driver, wait)
        advertisement_page = AdvertisementPage(driver, wait)
        
        main_page.open()
        main_page.click_place_ad_button()
        
        assert advertisement_page.get_modal_title(), "Window ttle is not visible"

#Создание объявления авторизованным пользователем
class TestAdvertisementPositive:
    @pytest.mark.positive
    def test_create_advertisement_authorized(self, driver, wait):
        main_page = MainPage(driver, wait)
        advertisement_page = AdvertisementPage(driver, wait)
        login_page = LoginPage(driver, wait)
        
        main_page.open()
        main_page.click_entry_button() #Нажать кнопку «Вход и регистрация».
        login_page.login_user("qa_python_25@mail.ru", "qa_python_25") #Заполнить все поля формы авторизации и нажать кнопку «Войти». 
        time.sleep(2) #сайт тормозит и кнопка не успевает появиться      
        # Создаем объявление
        main_page.click_place_ad_button()
                
        main_page.click_publish_ad_button()
        time.sleep(2) #сайт тормозит и кнопка не успевает появиться      