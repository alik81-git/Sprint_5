from selenium.webdriver.support import expected_conditions as EC
from locators import (
    MainPage,
    AdvertisementPageLocators,
    ProfilePageLocators,
    LoginPage,
    RegistartionPage,
)
from data import TestData


class TestCreateAds:

    def test_create_ad_authorized_user(self, driver, wait):

        # Выполнить регистрацию нового пользователя
        # Регистрация нового пользователя необходима, тк после 3х прогонов теста появляется пагинация,
        # Если использовать зарегистрированного пользователя
        ad_title = TestData.user_data()["title"]

        driver.find_element(*MainPage.LOGIN_BTN).click()
        wait.until(EC.visibility_of_element_located(LoginPage.LOGIN_LABEL))
        driver.find_element(*LoginPage.REGISTR_ACC_BTN).click()
        wait.until(EC.visibility_of_element_located(LoginPage.EMAIL_INPUT))
        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(TestData.random_email())
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(
            TestData.user_data()["password"]
        )
        driver.find_element(*RegistartionPage.CONFIRM_PASSWORD_INPUT).send_keys(
            TestData.user_data()["password"]
        )
        driver.find_element(*RegistartionPage.CREATE_ACC_BTN).click()

        wait.until(EC.visibility_of_element_located(MainPage.AVATAR_LOGO))
        wait.until(EC.visibility_of_element_located(MainPage.USER_NAME))

        # Заполнить формы и выбрать состояние товара
        driver.find_element(*MainPage.CREATE_AD_BUTTON).click()
        driver.find_element(*AdvertisementPageLocators.TITLE_INPUT).send_keys(ad_title)
        driver.find_element(
            *AdvertisementPageLocators.CONDITION_RADIOBUTTON_USED
        ).click()
        driver.find_element(*AdvertisementPageLocators.DESCRIPTION_TEXTAREA).send_keys(
            TestData.user_data()["description"]
        )
        driver.find_element(*AdvertisementPageLocators.PRICE_INPUT).send_keys(
            TestData.user_data()["price"]
        )

        # Выбрать последнюю категорию из dropdown категорий
        driver.find_element(*AdvertisementPageLocators.CATEGORY_DROPDOWN).click()
        wait.until(
            EC.visibility_of_element_located(AdvertisementPageLocators.LAST_CITY_OPTION)
        ).click()

        # Выбрать последний город из dropdown городов
        driver.find_element(*AdvertisementPageLocators.CITY_DROPDOWN).click()
        wait.until(
            EC.visibility_of_element_located(AdvertisementPageLocators.LAST_CITY_OPTION)
        ).click()

        # Опубликовать объявление
        driver.find_element(*AdvertisementPageLocators.SUBMIT_BUTTON).click()

        # Перейти в профиль пользователя
        # Используем driver.refresh, тк использование ожиданий не решило проблему с видимостью кнопки профиля
        driver.refresh()
        wait.until(EC.element_to_be_clickable(MainPage.AVATAR_LOGO))
        driver.find_element(*MainPage.AVATAR_LOGO).click()

        # Проверить наличие созданного объявления в списке объявлений
        wait.until(EC.element_to_be_clickable(ProfilePageLocators.AD_CARDS))
        advertisements_list = driver.find_elements(*ProfilePageLocators.AD_CARDS)
        assert len(advertisements_list) > 0, "Объявление не было создано"

        # Проверить актуальность созданного заголовка объявления в профиле
        ads_section = driver.find_element(*ProfilePageLocators.MY_ADS_SECTION)
        last_ad_title = ads_section.find_element(*ProfilePageLocators.AD_TITLE).text
        assert (
            last_ad_title == ad_title
        ), f"Заголовок {last_ad_title} отличается от {ad_title}"

    def test_create_ad_unauthorized_user(self, driver, wait):

        driver.find_element(*MainPage.CREATE_AD_BUTTON).click()
        auth_error = wait.until(
            EC.visibility_of_element_located(AdvertisementPageLocators.AUTH_ERROR)
        )
        assert (
            "Чтобы разместить объявление, авторизуйтесь" in auth_error.text
        ), f"текст не соответствует {auth_error.text}"
