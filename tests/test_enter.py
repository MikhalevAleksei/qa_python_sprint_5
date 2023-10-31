from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from gen_data_for_login import gen_data_email, gen_data_password, data_name


class TestEnter:


    def test_enter(self, driver, registration):
        user_name = 'Alex'
        user_email = 'test123@test.ru'
        user_password = '123456'

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.ENTER_ACCOUNT))
        driver.find_element(*Locators.ENTER_ACCOUNT).click()

        # WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        #     Locators.REF_REGISTRATION))
        # driver.find_element(*Locators.REF_REGISTRATION).click()
        # WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        #     Locators.INPUT_NAME))
        # fld_name = driver.find_element(*Locators.INPUT_NAME)
        # fld_name.send_keys(user_name)
        # fld_email = driver.find_element(*Locators.INPUT_EMAIL)
        # fld_email.send_keys(user_email)
        # fld_password = driver.find_element(*Locators.INPUT_PASSWORD)
        # fld_password.send_keys(user_password)
        # btn_registr = driver.find_element(*Locators.BUTTON_REGISTRATION)
        # btn_registr.click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.INPUT_EMAIL))
        driver.find_element(
            *Locators.INPUT_EMAIL).send_keys(gen_data_email)
        driver.find_element(
            *Locators.INPUT_PASSWORD).send_keys(gen_data_password)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.BUTTON_ENTER))
        driver.find_element(*Locators.BUTTON_ENTER).click()

#    def test_enter_main_page(self, driver):
        #main_page = driver.find_element(*ConstLocators.TEST_ENTER_MAIN_PAGE)
        # main_page = driver.find_element(
        #         By.XPATH, "//*[contains(@class,'button_button_size_large')]")
        # assert 'Оформить заказ' in main_page.text

    # def test_enter_personal_account(self, driver):
    #     driver.find_element(*ConstLocators.ENTER_ACCOUNT).click()
    #
    #     driver.find_element(
    #         *ConstLocators.INPUT_EMAIL).send_keys(gen_data_email)
    #     driver.find_element(*ConstLocators.INPUT_PASSWORD).send_keys(
    #         gen_data_password)
    #     driver.find_element(*ConstLocators.PERSONAL_ACCOUNT_ENTER).click()
    #
    #     assert ".site/account" in driver.current_url
    #
    # def test_enter_from_registration(self, driver):
    #     driver.find_element(*ConstLocators.ENTER_ACCOUNT).click()
    #     driver.find_element(*ConstLocators.REF_REGISTRATION).click()
    #     driver.find_element(*ConstLocators.REF_ENTER_FROM_REGISTRATION).click()
    #     driver.find_element(
    #         *ConstLocators.INPUT_EMAIL).send_keys(gen_data_email)
    #     driver.find_element(*ConstLocators.INPUT_PASSWORD).send_keys(
    #         gen_data_password)
    #     assert ".site" in driver.current_url
    #
    # def test_enter_from_password_restore(self, driver):
    #     driver.find_element(*ConstLocators.ENTER_ACCOUNT).click()
    #     driver.find_element(*ConstLocators.ENTER_FROM_PASSWORD_RESTORE).click()
    #     driver.find_element(*ConstLocators.REF_ENTER_FROM_REGISTRATION).click()
    #     driver.find_element(
    #         *ConstLocators.INPUT_EMAIL).send_keys(gen_data_email)
    #     driver.find_element(*ConstLocators.INPUT_PASSWORD).send_keys(
    #         gen_data_password)
    #     assert ".site" in driver.current_url

        driver.quit()
