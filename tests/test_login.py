from selenium.webdriver.support import expected_conditions as EC
from locators import MainPage
from locators import LoginPage
from data import TestData


class TestLogin:

    def test_user_login(self, driver, wait):

        driver.find_element(*MainPage.LOGIN_BTN).click()
        wait.until(EC.visibility_of_element_located(LoginPage.LOGIN_LABEL))

        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(
            TestData.user_data()["email"]
        )
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(
            TestData.user_data()["password"]
        )
        driver.find_element(*LoginPage.LOGIN_BTN).click()

        avatar_logo = wait.until(EC.visibility_of_element_located(MainPage.AVATAR_LOGO))
        user_name = wait.until(EC.visibility_of_element_located(MainPage.USER_NAME))

        assert avatar_logo.is_displayed(), "Аватар пользователя не отображается"
        assert user_name.is_displayed(), "Имя пользователя не отображается"
