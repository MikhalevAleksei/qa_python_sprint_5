import random as r

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import ConstLocators
from gen_data_for_login import gen_data_email, gen_data_password, data_name


class TestRegistration:
    def test_registration(self, driver):

        # driver = webdriver.Chrome()
        # driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*ConstLocators.REF_REGISTRATION).click()

        # data_name = "Alex"
        # gen_data_email = f'Aleksei_Mikhalev{r.randint(100, 900)}@yandex.ru'
        # gen_data_password = r.randint(123456, 654321)

        fld_name = driver.find_element(*ConstLocators.INPUT_NAME)
        fld_name.send_keys(data_name)

        fld_email = driver.find_element(*ConstLocators.INPUT_EMAIL)
        fld_email.send_keys(gen_data_email)

        fld_password = driver.find_element(By.NAME, "Пароль")
        fld_password.send_keys(gen_data_password)

        btn_enter = driver.find_element(By.XPATH, "//button[text()='Войти']")
        btn_enter.click()


if __name__ == '__main__':

    def test_ok_registration(self):
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_fld_name_not_empty(self):
        assert len(fld_name) > 0

# TODO
    def test_format_fld_email(self):
        pass

    def test_len_fld_password(self):
        assert len(fld_password) >= 6

#TODO
    def test_err_for_negative_login():
        test_registration(self,negative_login )


        driver.quit()
