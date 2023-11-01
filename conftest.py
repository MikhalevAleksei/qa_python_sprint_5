import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from data import GenDataLogin


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--window-size-1920,1080')
    driver = webdriver.Chrome(options=options)
    link = "https://stellarburgers.nomoreparties.site"
    driver.get(link)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def registration(driver):
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        Locators.ENTER_ACCOUNT))
    driver.find_element(*Locators.ENTER_ACCOUNT).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        Locators.REF_REGISTRATION))
    driver.find_element(*Locators.REF_REGISTRATION).click()

    fld_name = driver.find_element(*Locators.INPUT_NAME)
    fld_name.send_keys(GenDataLogin.data_name)
    fld_email = driver.find_element(*Locators.INPUT_EMAIL)
    fld_email.send_keys(GenDataLogin.gen_data_email)
    fld_password = driver.find_element(*Locators.INPUT_PASSWORD)
    fld_password.send_keys(GenDataLogin.gen_data_password)
    btn_registration = driver.find_element(*Locators.BUTTON_REGISTRATION)

    yield btn_registration.click()
    driver.quit()

@pytest.fixture(scope='function')
def enter(driver):
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        Locators.ENTER_ACCOUNT))
    driver.find_element(*Locators.ENTER_ACCOUNT).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        Locators.INPUT_EMAIL))
    driver.find_element(
        *Locators.INPUT_EMAIL).send_keys(GenDataLogin.gen_data_email)
    driver.find_element(
        *Locators.INPUT_PASSWORD).send_keys(GenDataLogin.gen_data_password)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        Locators.BUTTON_ENTER))
    btn_enter = driver.find_element(*Locators.BUTTON_ENTER).click()

    yield btn_enter
    driver.quit()


@pytest.fixture(scope='function')
def enter_account(driver):
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        Locators.ENTER_ACCOUNT))
    enter_account = driver.find_element(*Locators.ENTER_ACCOUNT).click()

    yield enter_account
    driver.quit()