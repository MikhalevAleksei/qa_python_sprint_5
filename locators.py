from selenium.webdriver.common.by import By


class Locators:
    # Поле ввода Войти в аккаунт
    BTN_ENTER_ACCOUNT = By.XPATH, "//*[text()='Войти в аккаунт']"

    BTN_ORDER = \
        By.XPATH, "//button[contains(@class, 'button_button_size_large')]"

    # Поле ввода имени
    INPUT_NAME = By.XPATH, "//*[text()='Имя']/following-sibling::input"

    # поле ввода email
    INPUT_EMAIL = By.XPATH, "//*[text()='Email']/following-sibling::input"

    # вход поле Пароль
    INPUT_PASSWORD = By.NAME, "Пароль"

    # вход кнопка Войти
    BTN_ENTER = (By.XPATH, "//button[text()='Войти']")

    # ссылка  Зарегистрироваться
    REF_REGISTRATION = By.XPATH, "//a[text()='Зарегистрироваться']"

    # ссылка  Восстановить пароль
    REF_RESTORE_PASSWORD = By.XPATH, "//*[text()='Восстановить пароль']"

    # вход в личный кабинет
    BTN_PERSONAL_ACCOUNT = By.XPATH, "//p[text()='Личный Кабинет']"

    # ссылка Войти в форме Регистрация
    REF_ENTER_FROM_REGISTRATION = By.XPATH, "//a[text()='Войти']"

    # ссылка Войти в через Восстановить пароль
    ENTER_FROM_PASSWORD_RESTORE = \
        By.XPATH, "//a[text()='Восстановить пароль']"

    BUTTON_REGISTRATION = By.XPATH, "//button[text()='Зарегистрироваться']"

    TEXT_PROFILE = By.XPATH, "//*[text()='Профиль']"

    TEST_ENTER_MAIN_PAGE = \
        By.XPATH, "//button[contains(@class,'button_button_size_large')]"

    MSG_ERROR_PASSWORD = By.XPATH, "//*[contains(@class, 'input__error ')]"
