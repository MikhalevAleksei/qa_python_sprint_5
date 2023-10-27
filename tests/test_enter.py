import random as r
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from . import locators

driver = webdriver.Chrome()
link = "https://stellarburgers.nomoreparties.site"
driver.get(link)

time.sleep(7)
#WebDriverWait(driver, 5).until(EC.visibility_of_element_located(By.XPATH,
# '//*[text()="Войти в аккаунт"]'))
#driver.find_element(By.XPATH, '//*[text()="Войти в аккаунт"]').click()
#WebDriverWait(driver, 5).until(EC.visibility_of_element_located(By.XPATH,
# '//*[text()="Войти"]'))
email = driver.find_element(By.NAME, "email")
password = driver.find_element(By.NAME, "password")

assert email.get_attribute('placeholder') == 'Email'
assert password.get_attribute('placeholder') == 'Пароль'

email = f'Aleksei_Mikhalev{r.randint(100, 900)}@yandex.ru'

driver.find_element(By.NAME, "name").send_keys(email)
driver.find_element(By.NAME, "Пароль").send_keys("QaPython2")
driver.find_element(By.TAG_NAME, "button[text()='Войти']").click()

entered_link = https://stellarburgers.nomoreparties.site/
assert driver.current_url == entered_link

driver.quit()
