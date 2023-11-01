from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import GenLogin
from locators import Locators


class TestRegistration:
    def test_registration(self, driver, registration):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.BTN_ENTER))
        assert '/login' in driver.current_url

    def test_len_fld_password(self, driver, registration):
        assert GenLogin.gen_password >= 6

    def test_fld_name_not_empty(self, driver, registration):
        assert len(GenLogin.data_name) > 0

    def test_err_msg_wrong_password(self, driver, enter_account):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.REF_REGISTRATION))
        driver.find_element(*Locators.REF_REGISTRATION).click()

        fld_name = driver.find_element(*Locators.INPUT_NAME)
        fld_name.send_keys(GenLogin.data_name)
        fld_email = driver.find_element(*Locators.INPUT_EMAIL)
        fld_email.send_keys(GenLogin.gen_email)
        fld_password = driver.find_element(*Locators.INPUT_PASSWORD)
        fld_password.send_keys(GenLogin.gen_wrong_password)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.MSG_ERROR_PASSWORD))
        driver.find_element(*Locators.MSG_ERROR_PASSWORD)
        err_msg = driver.find_element(*Locators.MSG_ERROR_PASSWORD)

        assert err_msg.text == "Некорректный пароль"

    def test_format_fld_email(self, driver, registration):
        assert '@yandex.ru' in GenLogin.gen_email

        driver.quit()
