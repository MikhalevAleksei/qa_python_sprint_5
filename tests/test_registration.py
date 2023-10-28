import random as r

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import locators
#
# class TestRegistration:
#     def test_registration(self, driver):

class TestRegistration:
    def test_registration(self, driver):

        # driver = webdriver.Chrome()
        # driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*locators.ConstLocators.REF_REGISTRATION).click()

        data_name = "Alex"
        gen_data_email = f'Aleksei_Mikhalev{r.randint(100, 900)}@yandex.ru'
        gen_data_password = r.randint(123456, 654321)

        driver.find_element(*locators.ConstLocators.INPUT_NAME).send_keys(data_name)
        driver.find_element(*locators.ConstLocators.INPUT_EMAIL).send_keys(
            gen_data_email)
        driver.find_element(By.NAME, "Пароль").send_keys("gen_data_password")
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()


        driver.quit()
