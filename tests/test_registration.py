from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from gen_data_for_login import GenDataLogin
from locators import Locators


class TestRegistration:
    def test_registration(self, driver, registration):

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.BUTTON_ENTER))
        assert '/login' in driver.current_url

    # def test_fld_name_not_empty(self, driver):
    #     WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
    #         Locators.ENTER_ACCOUNT))
    #     driver.find_element(*Locators.ENTER_ACCOUNT).click()
    #     fld_name = driver.find_element(*Locators.INPUT_NAME)
    #     assert len(fld_name.send_keys(data_name)) > 0

    def test_format_fld_email(self, driver, enter_account):
        fld_forma = driver.find_element(By.NAME, "name").get_attribute("value")
        assert '@ya.ru' in fld_forma

    def test_len_fld_password(self, driver, enter):
        # WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        #     Locators.ENTER_ACCOUNT))
        # driver.find_element(*Locators.ENTER_ACCOUNT).click()
        # WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        #     Locators.INPUT_EMAIL))
        # driver.find_element(
        #     *Locators.INPUT_EMAIL).send_keys(gen_data_email)
        # driver.find_element(
        #     *Locators.INPUT_PASSWORD).send_keys(gen_data_password)
        # WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        #     Locators.BUTTON_ENTER))
        # driver.find_element(*Locators.BUTTON_ENTER).click()
        len_password = driver.find_element(
            *Locators.INPUT_PASSWORD).send_keys(GenDataLogin.gen_data_password)
        assert len(len_password.get_attribute('value')) >= 6

    # def test_err_for_negative_login(self, driver):
    #     driver.find_element(*Locators.REF_REGISTRATION).click()
    #     fld_password = driver.find_element(By.NAME, "Пароль")
    #     fld_password.send_keys(gen_wrong_password)
    #     driver.find_element(*Locators.BUTTON_ENTER).click()
    #     WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
    #         Locators.MSG_ERROR_PASSWORD))
    #     elm = driver.find_element(Locators.MSG_ERROR_PASSWORD).text
    #     assert elm == "Некорректный пароль"

        driver.quit()
