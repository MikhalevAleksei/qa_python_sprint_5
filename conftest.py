import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from data import GenLogin
from urls import Urls


@pytest.fixture(scope='function')
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size-1920,1080')
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(Urls.url_main)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def registration(driver):
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
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
    return registration


@pytest.fixture(scope='function')
def enter(driver):
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        Locators.BTN_ENTER))
    driver.find_element(
        *Locators.INPUT_EMAIL).send_keys(GenLogin.gen_email)
    driver.find_element(
        *Locators.INPUT_PASSWORD).send_keys(GenLogin.gen_password)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        Locators.BTN_ENTER))
    driver.find_element(*Locators.BTN_ENTER).click()
    return enter


@pytest.fixture(scope='function')
def enter_account(driver):
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        Locators.BTN_ENTER_ACCOUNT))
    driver.find_element(*Locators.BTN_ENTER_ACCOUNT).click()
    return enter_account
