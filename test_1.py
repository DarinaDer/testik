from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('C:/Users/barsf/Downloads/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https://idemo.bspb.ru/login/success&prefetch_uri=https://idemo.bspb.ru/login/prefetch&force_new_session=true&state=/messages/form?type=message")
driver.set_window_size(1366,768)
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.ID, "login-otp-button").click()
driver.find_element(By.ID, "accounts-index").click()
driver.find_element(By.LINK_TEXT, "Открыть счёт").click()
driver.find_element(By.NAME, "condition.newAccountConditions").click()
driver.find_element(By.ID, "submit").click()
driver.find_element(By.CSS_SELECTOR, ".icon-close").click()
driver.close()
  
