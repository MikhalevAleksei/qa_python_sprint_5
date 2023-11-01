import random as r

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class GenLogin:
    data_name = "Alex"
    gen_email = f'Aleksei_Mikhalev{r.randint(100, 900)}@yandex.ru'
    gen_password = r.randint(123456, 654321)
    gen_wrong_password = r.randint(12345, 54321)


class User:
    test_name = 'Aleksei'
    test_email = 'Aleksei123@ya.ru'
    test_password = 123456

