from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import ConstLocators
from gen_data_for_login import gen_data_email, gen_data_password


class TestEnter:
    def test_enter(self, driver):
        link = "https://stellarburgers.nomoreparties.site"
        driver.get(link)
        reg_timer = By.XPATH, '//*[text()="Войти в аккаунт"]'
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(reg_timer))

        driver.find_element(*ConstLocators.ENTER_ACCOUNT).click()

        driver.find_element(*ConstLocators.INPUT_EMAIL).send_keys(gen_data_email)

        driver.find_element(*ConstLocators.INPUT_PASSWORD).send_keys(gen_data_password)

        enter_timer = By.XPATH, '//*[text()="Войти"]'
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(enter_timer))

        driver.find_element(*ConstLocators.BUTTON_ENTER).click()

    def test_enter_main_page(self, driver):
        assert ".site" in driver.current_url

    def test_enter_personal_account(self, driver):
        driver.find_element(*ConstLocators.ENTER_ACCOUNT).click()
        driver.find_element(*ConstLocators.PERSONAL_ACCOUNT_ENTER).click()
        driver.find_element(*ConstLocators.INPUT_EMAIL).send_keys(gen_data_email)
        driver.find_element(*ConstLocators.INPUT_PASSWORD).send_keys(
            gen_data_password)
        assert ".site" in driver.current_url

    def test_enter_from_registration(self, driver):
        driver.find_element(*ConstLocators.ENTER_ACCOUNT).click()
        driver.find_element(*ConstLocators.REF_REGISTRATION).click()
        driver.find_element(*ConstLocators.REF_ENTER_FROM_REGISTRATION).click()
        driver.find_element(*ConstLocators.INPUT_EMAIL).send_keys(gen_data_email)
        driver.find_element(*ConstLocators.INPUT_PASSWORD).send_keys(
            gen_data_password)
        assert ".site" in driver.current_url

    def test_enter_from_password_restore(self, driver):
        driver.find_element(*ConstLocators.ENTER_ACCOUNT).click()
        driver.find_element(*ConstLocators.ENTER_FROM_PASSWORD_RESTORE).click()
        driver.find_element(*ConstLocators.REF_ENTER_FROM_REGISTRATION).click()
        driver.find_element(*ConstLocators.INPUT_EMAIL).send_keys(gen_data_email)
        driver.find_element(*ConstLocators.INPUT_PASSWORD).send_keys(
            gen_data_password)
        assert ".site" in driver.current_url

        driver.quit()
