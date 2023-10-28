import random as r
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from qa_python_sprint_5 import locators

driver = webdriver.Chrome()
link = "https://stellarburgers.nomoreparties.site"
driver.get(link)

time.sleep(3)
#WebDriverWait(driver, 5).until(EC.visibility_of_element_located(By.XPATH,
# '//*[text()="Войти в аккаунт"]'))
#driver.find_element(By.XPATH, '//*[text()="Войти в аккаунт"]').click()
#WebDriverWait(driver, 5).until(EC.visibility_of_element_located(By.XPATH,
# '//*[text()="Войти"]'))
# email = driver.find_element(By.NAME, "email")
# password = driver.find_element(By.NAME, "password")
#
# assert email.get_attribute('placeholder') == 'Email'
# assert password.get_attribute('placeholder') == 'Пароль'

gen_data_email = f'Aleksei_Mikhalev{r.randint(100, 900)}@yandex.ru'
gen_data_password = r.randint(123456, 654321)

driver.find_element(By.XPATH, "//*[text()='Войти в аккаунт']").click()
time.sleep(4)
driver.find_element(By.NAME, "name").send_keys(gen_data_email)
time.sleep(4)
driver.find_element(By.NAME, "Пароль").send_keys(gen_data_password)
time.sleep(4)
driver.find_element(By.XPATH, "//*[text()='Войти']").click()

time.sleep(3)
current_url = driver.current_url
print(current_url)
assert current_url == link


driver.quit()
