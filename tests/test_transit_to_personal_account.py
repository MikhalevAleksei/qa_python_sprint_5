from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import gen_data_email, gen_data_password, data_name
from locators import Locators


class TestTransitPersonalAccount:
    def test_transit_to_account(self, driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.BTN_ENTER_ACCOUNT))
        driver.find_element(*Locators.BTN_ENTER_ACCOUNT).click()
        # WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        #     ConstLocators.REF_REGISTRATION))
        # driver.find_element(*ConstLocators.REF_REGISTRATION).click()
        # fld_name = driver.find_element(*ConstLocators.INPUT_NAME)
        # fld_name.send_keys(data_name)
        # fld_email = driver.find_element(*ConstLocators.INPUT_EMAIL)
        # fld_email.send_keys(gen_data_email)
        # fld_password = driver.find_element(*ConstLocators.INPUT_PASSWORD)
        # fld_password.send_keys(gen_data_password)
        # btn_registr = driver.find_element(*ConstLocators.BUTTON_REGISTRATION)
        # btn_registr.click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.INPUT_EMAIL))
        driver.find_element(
            *Locators.INPUT_EMAIL).send_keys(gen_data_email)
        print(gen_data_email)
        driver.find_element(
            *Locators.INPUT_PASSWORD).send_keys(gen_data_password)
        print(gen_data_password)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.BTN_ENTER))
        driver.find_element(*Locators.BTN_ENTER).click()

        driver.find_element(*Locators.BTN_PERSONAL_ACCOUNT).click()
        # WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        #     ConstLocators.TEXT_PROFILE))

        assert "/account/profile" in driver.current_url
        driver.quit()

