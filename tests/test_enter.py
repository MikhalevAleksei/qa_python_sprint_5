from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from data import GenLogin, User
from urls import Urls


class TestEnter:
    # def test_enter_main_page(self, driver, registration, enter):
    #     WebDriverWait(driver, 5).until(
    #         EC.element_to_be_clickable(Locators.BTN_ORDER))
    #     btn_is = driver.find_element(*Locators.BTN_ORDER)
    #     assert btn_is.text == 'Оформить заказ'
    #
    # def test_enter_personal_account(self, driver, registration):
    #     WebDriverWait(driver, 5).until(
    #         EC.element_to_be_clickable(Locators.BTN_PERSONAL_ACCOUNT))
    #     driver.find_element(*Locators.BTN_PERSONAL_ACCOUNT).click()
    #     WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
    #         Locators.BTN_ENTER))
    #     driver.find_element(
    #         *Locators.INPUT_EMAIL).send_keys(GenLogin.gen_email)
    #     driver.find_element(
    #         *Locators.INPUT_PASSWORD).send_keys(GenLogin.gen_password)
    #     WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
    #         Locators.BTN_ENTER))
    #     driver.find_element(*Locators.BTN_ENTER).click()
    #     WebDriverWait(driver, 5).until(
    #         EC.element_to_be_clickable(Locators.BTN_ORDER))
    #     btn_is = driver.find_element(*Locators.BTN_ORDER)
    #
    #     assert btn_is.text == 'Оформить заказ'

    def test_enter_from_registration(self, driver, enter_account):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.REF_REGISTRATION))
        driver.find_element(*Locators.REF_REGISTRATION).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.REF_ENTER_FROM_REGISTRATION))
        driver.find_element(*Locators.REF_ENTER_FROM_REGISTRATION).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.BTN_ENTER))
        driver.find_element(
            *Locators.INPUT_EMAIL).send_keys(User.test_email)
        driver.find_element(
            *Locators.INPUT_PASSWORD).send_keys(User.test_password)
        driver.find_element(*Locators.BTN_ENTER).click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.BTN_ORDER))
        btn_is = driver.find_element(*Locators.BTN_ORDER)

        assert btn_is.text == 'Оформить заказ'

 def test_enter_from_password_restore(self, driver):
    #     driver.find_element(*ConstLocators.ENTER_ACCOUNT).click()
    #     driver.find_element(*ConstLocators.ENTER_FROM_PASSWORD_RESTORE).click()
    #     driver.find_element(*ConstLocators.REF_ENTER_FROM_REGISTRATION).click()
    #     driver.find_element(
    #         *ConstLocators.INPUT_EMAIL).send_keys(gen_data_email)
    #     driver.find_element(*ConstLocators.INPUT_PASSWORD).send_keys(
    #         gen_data_password)
    #     assert ".site" in driver.current_url

        driver.quit()
