from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import User
from locators import Locators


def test_user_registration(driver):
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
    driver.find_element(*Locators.BUTTON_REGISTRATION)

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        Locators.BTN_ENTER))
    assert '/login' in driver.current_url
