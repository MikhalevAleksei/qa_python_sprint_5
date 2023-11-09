import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import GenLogin, User
from locators import Locators
from urls import Urls


class TestRegistration:
    def test_registration(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            Locators.BTN_ENTER_ACCOUNT))
        driver.find_element(*Locators.BTN_ENTER_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.REF_REGISTRATION))
        driver.find_element(*Locators.REF_REGISTRATION).click()

        fld_name = driver.find_element(*Locators.INPUT_NAME)
        fld_name.send_keys(GenLogin.data_name)
        fld_email = driver.find_element(*Locators.INPUT_EMAIL)
        fld_email.send_keys(GenLogin.gen_email)
        fld_password = driver.find_element(*Locators.INPUT_PASSWORD)
        fld_password.send_keys(GenLogin.gen_password)
        driver.find_element(*Locators.BTN_REGISTRATION).click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.REF_RESTORE_PASSWORD))
        assert driver.current_url == Urls.url_login
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.BTN_ENTER))
        driver.find_element(
            *Locators.INPUT_EMAIL).send_keys(GenLogin.gen_email)
        driver.find_element(
            *Locators.INPUT_PASSWORD).send_keys(GenLogin.gen_password)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.BTN_ENTER))
        driver.find_element(*Locators.BTN_ENTER).click()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.BTN_PERSONAL_ACCOUNT))
        driver.find_element(*Locators.BTN_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.BTN_EXIT_PERSONAL_ACCOUNT))
        actual_name = driver.find_element(*Locators.INPUT_NAME)
        expected_name = GenLogin.data_name
        assert actual_name.get_attribute('value') == expected_name

    @pytest.mark.parametrize('wrong_password', User.wrong_passwords_list)
    def test_err_msg_if_password_less_6_symbols(self, driver, enter_account,
                                                wrong_password):

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.REF_REGISTRATION))
        driver.find_element(*Locators.REF_REGISTRATION).click()

        fld_name = driver.find_element(*Locators.INPUT_NAME)
        fld_name.send_keys(GenLogin.data_name)
        fld_email = driver.find_element(*Locators.INPUT_EMAIL)
        fld_email.send_keys(GenLogin.gen_email)
        fld_password = driver.find_element(*Locators.INPUT_PASSWORD)
        fld_password.send_keys(wrong_password)
        driver.find_element(*Locators.BTN_REGISTRATION).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.MSG_ERROR_PASSWORD))
        driver.find_element(*Locators.MSG_ERROR_PASSWORD)
        err_msg = driver.find_element(*Locators.MSG_ERROR_PASSWORD)

        assert err_msg.text == "Некорректный пароль"

    def test_format_fld_email(self, driver, enter_account):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.BTN_ENTER))
        driver.find_element(
            *Locators.INPUT_EMAIL).send_keys(GenLogin.gen_email)
        driver.find_element(
            *Locators.INPUT_PASSWORD).send_keys(GenLogin.gen_password)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.BTN_ENTER))
        driver.find_element(*Locators.BTN_ENTER).click()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.BTN_PERSONAL_ACCOUNT))
        driver.find_element(*Locators.BTN_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                Locators.BTN_EXIT_PERSONAL_ACCOUNT))
        actual_email = driver.find_element(*Locators.VALUE_EMAIL)
        expected_email = GenLogin.gen_email
        assert actual_email.get_attribute('value') == expected_email
        assert '@yandex.ru' in actual_email.get_attribute('value')

    def test_registration_fld_name_empty(self, driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.BTN_ENTER_ACCOUNT))
        driver.find_element(*Locators.BTN_ENTER_ACCOUNT).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.REF_REGISTRATION))
        driver.find_element(*Locators.REF_REGISTRATION).click()

        fld_name = driver.find_element(*Locators.INPUT_NAME)
        fld_name.send_keys(User.test_name)
        fld_email = driver.find_element(*Locators.INPUT_EMAIL)
        fld_email.send_keys(User.test_email)
        fld_password = driver.find_element(*Locators.INPUT_PASSWORD)
        fld_password.send_keys(User.test_password)
        driver.find_element(*Locators.BTN_REGISTRATION).click()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.BTN_PERSONAL_ACCOUNT))
        driver.find_element(*Locators.BTN_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                Locators.BTN_EXIT_PERSONAL_ACCOUNT))
        actual_name = driver.find_element(*Locators.INPUT_NAME)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.BTN_ENTER))
        driver.find_element(
            *Locators.INPUT_EMAIL).send_keys(User.test_email)
        driver.find_element(
            *Locators.INPUT_PASSWORD).send_keys(User.test_password)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.BTN_ENTER))
        driver.find_element(*Locators.BTN_ENTER).click()
        assert len(actual_name) > 0



