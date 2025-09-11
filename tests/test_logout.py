from selenium.webdriver.support import expected_conditions as EC
from locators import MainPage, LoginPage
from data import TestData


class TestLogOut:

    def test_user_logout(self, driver, wait):

        # Выполнить Авторизацию пользователя
        driver.find_element(*MainPage.LOGIN_BTN).click()
        wait.until(EC.visibility_of_element_located(LoginPage.LOGIN_LABEL))
        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(
            TestData.user_data()["email"]
        )
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(
            TestData.user_data()["password"]
        )
        driver.find_element(*LoginPage.LOGIN_BTN).click()
        wait.until(EC.visibility_of_element_located(MainPage.AVATAR_LOGO))
        wait.until(EC.visibility_of_element_located(MainPage.USER_NAME))

        # Разлогин пользователя
        logout_btn = wait.until(EC.element_to_be_clickable(MainPage.LOGOUT_BTN))
        avatar_logo = driver.find_elements(*MainPage.AVATAR_LOGO)
        user_name = driver.find_elements(*MainPage.USER_NAME)
        logout_btn.click()

        login_btn = wait.until(EC.element_to_be_clickable(MainPage.LOGIN_BTN))

        assert login_btn.is_displayed
        assert not len(avatar_logo) == 0, "Аватар пользователя отображается"
        assert not len(user_name) == 0, "Имя пользователя отображается"
