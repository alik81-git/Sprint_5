from selenium.webdriver.common.by import By


class MainPage:
    LOGIN_BTN = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    AVATAR_LOGO = (By.CLASS_NAME, "circleSmall")
    USER_NAME = (By.XPATH, "//h3[@class='profileText name']")
    LOGOUT_BTN = (By.XPATH, "//button[text()='Выйти']")
    CREATE_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")


class LoginPage:
    LOGIN_LABEL = (By.XPATH, "//h1[text()='Войти']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[text()='Войти']")
    REGISTR_ACC_BTN = (By.XPATH, "//button[text()='Нет аккаунта']")


class RegistartionPage:
    REGISTRATION_LABEL = (By.XPATH, "//h1[text()='Зарегистрироваться']")
    CONFIRM_PASSWORD_INPUT = (By.NAME, "submitPassword")
    CREATE_ACC_BTN = (By.XPATH, "//button[text()='Создать аккаунт']")
    EMAIL_ERROR = (By.XPATH, "//span[@class='input_span__yWPqB' and text()='Ошибка']")


class AdvertisementPageLocators:
    TITLE_INPUT = (By.NAME, "name")
    DESCRIPTION_TEXTAREA = (By.XPATH, "//textarea[@placeholder='Описание товара']")
    PRICE_INPUT = (By.NAME, "price")
    CATEGORY_DROPDOWN = (By.CSS_SELECTOR, "input[name='category'] + button")
    CATEGORY_OPTIONS = (By.XPATH, "//div[@class='dropDownMenu_options__CmHmm']/button")
    LAST_CATEGORY = (
        By.XPATH,
        "(//div[@class='dropDownMenu_options__CmHmm']/button)[last()]",
    )
    CITY_DROPDOWN = (By.CSS_SELECTOR, "input[name='city'] + button")
    CITY_OPTIONS = (By.XPATH, "//div[@data-test='city-select-menu']//button")
    LAST_CITY_OPTION = (
        By.XPATH,
        "(//div[@class='dropDownMenu_options__CmHmm']/button)[last()]",
    )
    CONDITION_RADIOBUTTON_NEW = (
        By.XPATH,
        "//div[@class='radioUnput_inputActive__eC-HY']",
    )
    CONDITION_RADIOBUTTON_USED = (
        By.XPATH,
        "//div[@class='radioUnput_inputRegular__FbVbr']",
    )
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")
    AUTH_ERROR = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")


class ProfilePageLocators:
    MY_ADS_SECTION = (
        By.XPATH,
        "//h1[contains(text(),'Мои объявления')]/following-sibling::div//div[@class='grid_threeColumns__ldn5D']",
    )
    AD_TITLE = (By.XPATH, ".//h2[@class='h2']")
    AD_CARDS = (
        By.XPATH,
        "//div[contains(@class, 'grid_threeColumns__ldn5D')]//div[@class='card']",
    )
