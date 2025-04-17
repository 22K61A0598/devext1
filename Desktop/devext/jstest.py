from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/add.html")
driver.find_element(By.ID, "num1").send_keys("10")
driver.find_element(By.ID, "num2").send_keys("15")
driver.find_element(By.TAG_NAME, "button").click()
result = driver.find_element(By.ID, "result").text
time.sleep(6)
driver.quit()   