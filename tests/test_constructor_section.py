from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestConstructorSection:
    def test_constructor_section_burgers(self, driver):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.BTN_PERSONAL_ACCOUNT))
        driver.find_element(*Locators.BTN_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                Locators.BTN_TRANSIT_TO_CONSTRUCTOR))
        driver.find_element(*Locators.BTN_TRANSIT_TO_CONSTRUCTOR).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.BTN_BUL))

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.TXT_BUL))
        element = driver.find_element(*Locators.TXT_BUL)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        btn_is = driver.find_element(*Locators.TXT_BUL)

        assert btn_is.text == 'Булки'

    def test_constructor_section_souses(self, driver):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.BTN_PERSONAL_ACCOUNT))
        driver.find_element(*Locators.BTN_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                Locators.BTN_TRANSIT_TO_CONSTRUCTOR))
        driver.find_element(*Locators.BTN_TRANSIT_TO_CONSTRUCTOR).click()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.BTN_SOUSES))
        driver.find_element(*Locators.BTN_SOUSES).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.TXT_SOUSES))
        btn_is = driver.find_element(*Locators.TXT_SOUSES)

        assert btn_is.text == 'Соусы'

    def test_constructor_section_staffing(self, driver):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.BTN_PERSONAL_ACCOUNT))
        driver.find_element(*Locators.BTN_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                Locators.BTN_TRANSIT_TO_CONSTRUCTOR))
        driver.find_element(*Locators.BTN_TRANSIT_TO_CONSTRUCTOR).click()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.BTN_STAFFING))
        driver.find_element(*Locators.BTN_STAFFING).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.TXT_STAFFING))
        btn_is = driver.find_element(*Locators.TXT_STAFFING)

        assert btn_is.text == 'Начинки'
        driver.quit()
