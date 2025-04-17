from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
chrome_driver_path = "C:/Users/91934/Downloads/chromedriver-win64 (2)/chromedriver-win64/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")
time.sleep(5)
driver.quit()
