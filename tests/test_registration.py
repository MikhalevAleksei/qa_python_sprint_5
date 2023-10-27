import random as r

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from . import locators

class TestRegistration:
    def test_registration(self, driver):

# driver = webdriver.Chrome()
# driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.TAG_NAME, *ANCOR_REGISTRATION).click()

    email = f'Aleksei_Mikhalev{r.randint(100, 900)}@yandex.ru'

    driver.find_element(*INPUT_NAME).send_keys("Alex")
    driver.find_element(*INPUT_EMAIL).send_keys(email)
    driver.find_element(By.NAME, "Пароль").send_keys("QaPython2")
    driver.find_element(By.TAG_NAME, "button[text()='Войти']").click()


driver.quit()
