from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import ConstLocators
from gen_data_for_login import gen_data_email, gen_data_password, data_name


class TestEnter:
    def test_enter(self, driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            ConstLocators.ENTER_ACCOUNT))
        driver.find_element(*ConstLocators.ENTER_ACCOUNT).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            ConstLocators.REF_REGISTRATION))
        driver.find_element(*ConstLocators.REF_REGISTRATION).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            ConstLocators.INPUT_NAME))
        fld_name = driver.find_element(*ConstLocators.INPUT_NAME)
        fld_name.send_keys(data_name)
        fld_email = driver.find_element(*ConstLocators.INPUT_EMAIL)
        fld_email.send_keys(gen_data_email)
        fld_password = driver.find_element(*ConstLocators.INPUT_PASSWORD)
        fld_password.send_keys(gen_data_password)
        btn_registr = driver.find_element(*ConstLocators.BUTTON_REGISTRATION)
        btn_registr.click()

        driver.find_element(
            *ConstLocators.INPUT_EMAIL).send_keys(gen_data_email)
        driver.find_element(
            *ConstLocators.INPUT_PASSWORD).send_keys(gen_data_password)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            ConstLocators.BUTTON_ENTER))
        driver.find_element(*ConstLocators.BUTTON_ENTER).click()

    def test_enter_main_page(self, driver):
        assert ".site" in driver.current_url

    def test_enter_personal_account(self, driver):
        driver.find_element(*ConstLocators.ENTER_ACCOUNT).click()
        driver.find_element(*ConstLocators.PERSONAL_ACCOUNT_ENTER).click()
        driver.find_element(
            *ConstLocators.INPUT_EMAIL).send_keys(gen_data_email)
        driver.find_element(*ConstLocators.INPUT_PASSWORD).send_keys(
            gen_data_password)
        assert ".site" in driver.current_url

    def test_enter_from_registration(self, driver):
        driver.find_element(*ConstLocators.ENTER_ACCOUNT).click()
        driver.find_element(*ConstLocators.REF_REGISTRATION).click()
        driver.find_element(*ConstLocators.REF_ENTER_FROM_REGISTRATION).click()
        driver.find_element(
            *ConstLocators.INPUT_EMAIL).send_keys(gen_data_email)
        driver.find_element(*ConstLocators.INPUT_PASSWORD).send_keys(
            gen_data_password)
        assert ".site" in driver.current_url

    def test_enter_from_password_restore(self, driver):
        driver.find_element(*ConstLocators.ENTER_ACCOUNT).click()
        driver.find_element(*ConstLocators.ENTER_FROM_PASSWORD_RESTORE).click()
        driver.find_element(*ConstLocators.REF_ENTER_FROM_REGISTRATION).click()
        driver.find_element(
            *ConstLocators.INPUT_EMAIL).send_keys(gen_data_email)
        driver.find_element(*ConstLocators.INPUT_PASSWORD).send_keys(
            gen_data_password)
        assert ".site" in driver.current_url

        driver.quit()
