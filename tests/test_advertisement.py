import pytest
import os, sys
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_main import MainPage
from page_login import LoginPage
from page_advertisement import AdvertisementPage


# Создание объявления неавторизованным пользователем
class TestAdvertisementNegative:
    @pytest.mark.negative
    def test_create_advertisement_unauthorized(self, driver, wait):
        main_page = MainPage(driver, wait)
        advertisement_page = AdvertisementPage(driver, wait)

        main_page.open()
        main_page.click_place_ad_button()

        assert advertisement_page.get_modal_title(), "Window ttle is not visible"


# Создание объявления авторизованным пользователем
class TestAdvertisementPositive:
    @pytest.mark.positive
    def test_create_advertisement_authorized(self, driver, wait):
        main_page = MainPage(driver, wait)
        advertisement_page = AdvertisementPage(driver, wait)
        login_page = LoginPage(driver, wait)

        main_page.open()
        main_page.click_entry_button()  # Нажать кнопку «Вход и регистрация».
        login_page.login_user(
            "qa_python_25@mail.ru", "qa_python_25"
        )  # Заполнить все поля формы авторизации и нажать кнопку «Войти».

        time.sleep(2)  # сайт тормозит и кнопка не успевает появиться

        # Создаем объявление
        main_page.click_place_ad_button()

        # Здесь заполнить объявление
        advertisement_page.set_item_name()
        advertisement_page.set_item_description()
        advertisement_page.set_item_price()
        advertisement_page.set_item_radio_used()
        advertisement_page.set_item_city_dropdown()
        advertisement_page.set_item_lastcity()
        advertisement_page.set_item_category_dropdown()
        advertisement_page.set_item_lastcategory()
        main_page.click_publish_ad_button()
        time.sleep(2)  # сайт тормозит и кнопка не успевает появиться
        main_page.go_profile()
        time.sleep(2)  # сайт тормозит и кнопка не успевает появиться
        assert main_page.search_item_name
