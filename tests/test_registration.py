from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPage
from locators import MainPage
from locators import RegistartionPage
from data import TestData


class TestRegistration:

    def test_new_user_registration_valid_email_format(self, driver, wait):

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

        avatar_logo = wait.until(EC.visibility_of_element_located(MainPage.AVATAR_LOGO))
        user_name = wait.until(EC.visibility_of_element_located(MainPage.USER_NAME))

        assert avatar_logo.is_displayed(), "Аватар пользователя не отображается"
        assert user_name.is_displayed(), "Имя пользователя не отображается"

    def test_new_user_registration_unsupported_email_format(self, driver, wait):

        driver.find_element(*MainPage.LOGIN_BTN).click()
        wait.until(EC.visibility_of_element_located(LoginPage.LOGIN_LABEL))

        driver.find_element(*LoginPage.REGISTR_ACC_BTN).click()
        wait.until(EC.visibility_of_element_located(LoginPage.EMAIL_INPUT))
        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(
            TestData.user_data()["unsupported_email"]
        )
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(
            TestData.user_data()["password"]
        )
        driver.find_element(*RegistartionPage.CONFIRM_PASSWORD_INPUT).send_keys(
            TestData.user_data()["password"]
        )
        driver.find_element(*RegistartionPage.CREATE_ACC_BTN).click()

        email_error = wait.until(
            EC.visibility_of_element_located(RegistartionPage.EMAIL_ERROR)
        )
        assert email_error.is_displayed(), "Ошибка не появилась"

    def test_registration_already_registered_user(self, driver, wait):

        driver.find_element(*MainPage.LOGIN_BTN).click()
        wait.until(EC.visibility_of_element_located(LoginPage.LOGIN_LABEL))

        driver.find_element(*LoginPage.REGISTR_ACC_BTN).click()
        wait.until(EC.visibility_of_element_located(LoginPage.EMAIL_INPUT))
        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(
            TestData.user_data()["email"]
        )
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(
            TestData.user_data()["password"]
        )
        driver.find_element(*RegistartionPage.CONFIRM_PASSWORD_INPUT).send_keys(
            TestData.user_data()["password"]
        )
        driver.find_element(*RegistartionPage.CREATE_ACC_BTN).click()

        email_error = wait.until(
            EC.visibility_of_element_located(RegistartionPage.EMAIL_ERROR)
        )
        assert email_error.is_displayed(), "Ошибка не появилась"
