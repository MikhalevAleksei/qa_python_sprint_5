from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestTransitFromPersonalAccountToConstructor:
    def test_transit_from_personal_account_to_constructor(self, driver,
                                                     registration, enter):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.BTN_PERSONAL_ACCOUNT))
        driver.find_element(*Locators.BTN_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.BTN_TRANSIT_TO_CONSTRUCTOR))
        driver.find_element(*Locators.BTN_TRANSIT_TO_CONSTRUCTOR).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.TXT_CONSTRUCT_BURGERS))
        btn_is = driver.find_element(*Locators.TXT_CONSTRUCT_BURGERS)

        assert btn_is.text == 'Соберите бургер'

    def test_transit_from_personal_account_to_logo(self, driver, registration,
                                                   enter):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.BTN_PERSONAL_ACCOUNT))
        driver.find_element(*Locators.BTN_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.LOGO))
        driver.find_element(*Locators.LOGO).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.TXT_CONSTRUCT_BURGERS))
        btn_is = driver.find_element(*Locators.TXT_CONSTRUCT_BURGERS)

        assert btn_is.text == 'Соберите бургер'

        driver.quit()

