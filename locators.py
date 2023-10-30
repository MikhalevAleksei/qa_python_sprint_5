from selenium.webdriver.common.by import By


class ConstLocators:
    # Поле ввода Войти в аккаунт
    ENTER_ACCOUNT = By.XPATH, "//*[text()='Войти в аккаунт']"

    # Поле ввода имени
    INPUT_NAME = By.XPATH, "//*[text()='Имя']/following-sibling::input"

    # поле ввода email
    INPUT_EMAIL = By.XPATH, "//*[text()='Email']/following-sibling::input"

    # вход поле Пароль
    INPUT_PASSWORD = (By.NAME, "Пароль")

    # вход кнопка Войти
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")

    # ссылка  Зарегистрироваться
    REF_REGISTRATION = (By.XPATH, "//*[text()='Зарегистрироваться']")

    # ссылка  Восстановить пароль
    REF_RESTORE_PASSWORD = (By.XPATH, "//*[text()='Восстановить пароль']")

    # вход в личный кабинет
    PERSONAL_ACCOUNT_ENTER = (By.XPATH, "//*[text()='Личный Кабинет']")

    # ссылка Войти в форме Регистрация
    REF_ENTER_FROM_REGISTRATION = (By.XPATH, "//a[text()='Войти']")

    # ссылка Войти в через Восстановить пароль
    ENTER_FROM_PASSWORD_RESTORE = (By.XPATH, "//a[text()='Восстановить пароль']")
