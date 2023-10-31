from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from gen_data_for_login import gen_data_email, gen_data_password, data_name
from locators import Locators


class TestTransitFromPersonalAccountToConstructor:
    def test_from_account_to_constructor(self, driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.ENTER_ACCOUNT))
        driver.find_element(*Locators.ENTER_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.REF_REGISTRATION))
        driver.find_element(*Locators.REF_REGISTRATION).click()
        fld_name = driver.find_element(*Locators.INPUT_NAME)
        fld_name.send_keys(data_name)
        fld_email = driver.find_element(*Locators.INPUT_EMAIL)
        fld_email.send_keys(gen_data_email)
        fld_password = driver.find_element(*Locators.INPUT_PASSWORD)
        fld_password.send_keys(gen_data_password)
        btn_registr = driver.find_element(*Locators.BUTTON_REGISTRATION)
        btn_registr.click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.INPUT_EMAIL))
        driver.find_element(
            *Locators.INPUT_EMAIL).send_keys(gen_data_email)
        driver.find_element(
            *Locators.INPUT_PASSWORD).send_keys(gen_data_password)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.BUTTON_ENTER))
        driver.find_element(*Locators.BUTTON_ENTER).click()

        driver.find_element(*Locators.PERSONAL_ACCOUNT_ENTER).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.TEXT_PROFILE))
        driver.find_element(By.XPATH, "//p[text()='Конструктор']").click()
        assert ".site/account/profile" in driver.current_url
        driver.quit()
