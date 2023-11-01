from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestExitFromPersonalAccount:
    def test_exit_from_personal_account(self, driver, registration, enter):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.BTN_PERSONAL_ACCOUNT))
        driver.find_element(*Locators.BTN_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.BTN_EXIT_PERSONAL_ACCOUNT))
        driver.find_element(*Locators.BTN_EXIT_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.BTN_ENTER))

        assert '/login' in driver.current_url
