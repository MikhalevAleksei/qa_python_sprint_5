from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from gen_data_for_login import gen_data_email, gen_data_password, data_name
from locators import ConstLocators


class TestTransitPersonalAccount:
    def test_transit(self, driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            ConstLocators.ENTER_ACCOUNT))
        driver.find_element(*ConstLocators.ENTER_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            ConstLocators.REF_REGISTRATION))
        driver.find_element(*ConstLocators.REF_REGISTRATION).click()
        fld_name = driver.find_element(*ConstLocators.INPUT_NAME)
        fld_name.send_keys(data_name)
        fld_email = driver.find_element(*ConstLocators.INPUT_EMAIL)
        fld_email.send_keys(gen_data_email)
        fld_password = driver.find_element(*ConstLocators.INPUT_PASSWORD)
        fld_password.send_keys(gen_data_password)


        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            ConstLocators.ENTER_ACCOUNT))
        fld_email = driver.find_element(*ConstLocators.INPUT_EMAIL)
        fld_email.send_keys(gen_data_email)
        fld_password = driver.find_element(*ConstLocators.INPUT_PASSWORD)
        fld_password.send_keys(gen_data_password)

        driver.find_element(*ConstLocators.PERSONAL_ACCOUNT_ENTER).click()

        assert "/account/profile" in driver.current_url
        driver.quit()

