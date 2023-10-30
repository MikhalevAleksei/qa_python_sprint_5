import random as r

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import ConstLocators
from gen_data_for_login import gen_data_email, gen_data_password, data_name


class TestRegistration:
    def test_registration(self, driver):

        driver.find_element(*ConstLocators.REF_REGISTRATION).click()

        fld_name = driver.find_element(*ConstLocators.INPUT_NAME)
        fld_name.send_keys(data_name)

        fld_email = driver.find_element(*ConstLocators.INPUT_EMAIL)
        fld_email.send_keys(gen_data_email)

        fld_password = driver.find_element(By.NAME, "Пароль")
        fld_password.send_keys(gen_data_password)
        len_password = fld_password.send_keys(gen_data_password)

        btn_enter = driver.find_element(By.XPATH, "//button[text()='Войти']")
        btn_enter.click()


    def test_ok_registration(self, driver):
         assert '/login' in driver.current_url

    def test_fld_name_not_empty(self, driver):
        assert len(self.fld_name) > 0

    def test_format_fld_email(self, driver):
        fld_forma = driver.find_element(By.NAME, "name").get_attribute("value")
        assert '123@ya.ru' in fld_forma

    def test_len_fld_password(self, driver):
        assert len(self.len_password) >= 6


    def test_err_for_negative_login(self, driver):
        driver.find_element(*ConstLocators.REF_REGISTRATION).click()
        fld_password = driver.find_element(By.NAME, "Пароль")
        fld_password.send_keys('12345')
        elm = driver.find_element(By.CSS_SELECTOR, ".input_error").text
        assert elm == "Некорректный пароль"

        driver.quit()
