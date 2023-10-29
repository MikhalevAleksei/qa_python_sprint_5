import pytest
from selenium.webdriver.chrome import webdriver


class UserRegistration:
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password

    @pytest.fixture()
    def correct_user(self):
        return {name: "Alex", login: "AlexMaksimov123@yandex.ru",
                password: "123456"}

    @pytest.fixture()
    def negative_user(self):
        return {name: "Alex", login: "AlexMaksimov654@yandex.ru", /
               password: "12345"}

        @pytest.fixture(scope='function')
        def driver():
            webdriver_options = webdriver.ChromeOptions()
            # webdriver_options.add_argument('--headless')
            webdriver_options.add_argument('--window-size=640,480')
            # driver = webdriver.Chrome(options=webdriver_options)

            driver = webdriver.Chrome(ChromeDriverManadger().install())
            driver.get("https://stellarburgers.nomoreparties.site/login")
            yield driver
            driver.quit()
