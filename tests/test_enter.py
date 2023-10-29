import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import test_registration

from locators import ConstLocators
from gen_data_for_login import gen_data_email, gen_data_password

driver = webdriver.Chrome()
link = "https://stellarburgers.nomoreparties.site"
driver.get(link)

reg_timer = By.XPATH, '//*[text()="Войти в аккаунт"]'
WebDriverWait(driver, 5).until(EC.visibility_of_element_located(reg_timer))

#TODO
# email = driver.find_element(By.NAME, "email")
# password = driver.find_element(By.NAME, "password")
# assert email.get_attribute('placeholder') == 'Email'
# assert password.get_attribute('placeholder') == 'Пароль'

driver.find_element(*ConstLocators.ENTER_ACCOUNT).click()

driver.find_element(*ConstLocators.INPUT_EMAIL).send_keys(gen_data_email)

driver.find_element(*ConstLocators.INPUT_PASSWORD).send_keys(gen_data_password)

enter_timer = By.XPATH, '//*[text()="Войти"]'
WebDriverWait(driver, 5).until(EC.visibility_of_element_located(enter_timer))

driver.find_element(*ConstLocators.BUTTON_ENTER).click()

#TODO
time.sleep(3)
current_url = driver.current_url
print(current_url)



driver.quit()
