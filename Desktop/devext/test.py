from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
path = "http://127.0.0.1:5000"
driver.get(path)
time.sleep(2)
driver.find_element(By.NAME, "name").send_keys("Test User")
driver.find_element(By.NAME, "email").send_keys("test@example.com")
driver.find_element(By.NAME, "password").send_keys("strongpass")
driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
time.sleep(3)
print("Current URL:", driver.current_url)
driver.quit()