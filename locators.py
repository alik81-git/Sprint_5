from selenium.webdriver.common.by import By


class MainPageLocators:
    ENTRY_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    PLACE_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    PUBLISH_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")
    GO_PROFILE = (By.XPATH, "//button[@class='circleSmall']")
    USER_AVATAR = (
        By.XPATH,
        "/html/body/div/div/div[1]/div/div[1]/button[@profileText name='User.']",
    )
    USER_NAME = (
        By.XPATH,
        "html/body/div/div/div[1]/div/div[1]/div/h3[@profileText name='User.']",
    )
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")
    FIND_ITEM_NAME = (By.XPATH, ".//h2[@class='h2']")


class RegistrationPageLocators:
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    SUBMIT_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='submitPassword']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-testid='error-message']")
    ERROR_FIELD = (By.CSS_SELECTOR, ".error-field")
    ERROR_EMAIL = (
        By.XPATH,
        "html/body/div/div/div[2]/div[5]/form/div[2]/div[1]/div/div[@class='input_inputError__fLUP9']",
    )
    ERROR_PASSWORD = (
        By.XPATH,
        "html/body/div/div/div[2]/div[5]/form/div[2]/div[2]/div/div[@class='input_inputError__fLUP9']",
    )
    ERROR_SUBMIT_PASSWORD = (
        By.XPATH,
        "html/body/div/div/div[2]/div[5]/form/div[2]/div[3]/div/div[@class='input_inputError__fLUP9']",
    )
    ERROR_TEXT_FIELD = (
        By.XPATH,
        "html/body/div/div/div[2]/div[5]/form/div[2]/div[1]/span[@input_span__yWPqB='Ошибка']",
    )


class LoginPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")


class AdvertisementPageLocators:
    MODAL_TITLE = (
        By.XPATH,
        "html/body/div/div/div[2]/div[5]/form/div[1]/h1[text()='Чтобы разместить объявление, авторизуйтесь']",
    )
    ITEM_NAME = (
        By.XPATH,
        "html/body/div/div/div[2]/div/form/div[2]/div[1]/div/div/input",
    )
    ITEM_DESCRIPTION = (
        By.XPATH,
        "html/body/div/div/div[2]/div/form/div[4]/div/textarea",
    )
    ITEM_PRICE = (By.XPATH, "html/body/div/div/div[2]/div/form/div[5]/div/div/input")
    ITEM_RADIO_NEW = (
        By.XPATH,
        "html/body/div/div/div[2]/div/form/fieldset/div/div[1]/div",
    )  # новое <div class="radioUnput_inputActive__eC-HY"></div>
    ITEM_RADIO_USED = (
        By.XPATH,
        "html/body/div/div/div[2]/div/form/fieldset/div/div[2]/div",
    )  # б/у   <div class="radioUnput_inputRegular__FbVbr"></div>
    ITEM_CITY_DROPDOWN = (
        By.XPATH,
        "html/body/div/div/div[2]/div/form/div[3]/div[1]/button",
    )
    ITEM_LAST_CITY = (
        By.XPATH,
        "html/body/div/div/div[2]/div/form/div[3]/div[2]/button[6]/span",
    )
    ITEM_CATEGORY_DROPDOWN = (
        By.XPATH,
        "html/body/div/div/div[2]/div/form/div[2]/div[2]/div[1]/button",
    )
    ITEM_LAST_CATEGORY = (
        By.XPATH,
        "html/body/div/div/div[2]/div/form/div[2]/div[2]/div[2]/button[5]/span",
    )

    TITLE_INPUT = (By.CSS_SELECTOR, "input[name='title']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[name='description']")
    PRICE_INPUT = (By.CSS_SELECTOR, "input[name='price']")
    CATEGORY_DROPDOWN = (By.CSS_SELECTOR, "select[name='category']")
    CITY_DROPDOWN = (By.CSS_SELECTOR, "select[name='city']")
    CONDITION_RADIO = (By.CSS_SELECTOR, "input[name='condition']")
    PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")
    MY_ADVERTISEMENTS = (By.CSS_SELECTOR, "[data-testid='my-advertisements']")
    ADVERTISEMENT_ITEM = (By.CSS_SELECTOR, "[data-testid='advertisement-item']")
