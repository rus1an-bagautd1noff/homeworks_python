from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/inputs")
    time.sleep(2)

    number_input = driver.find_element(By.XPATH, '//input[@type="number"]')
    number_input.send_keys("Sky")
    time.sleep(2)

    number_input.clear()
    time.sleep(2)

    number_input = driver.find_element(By.XPATH, '//input[@type="number"]')
    number_input.send_keys("Pro")
    time.sleep(2)

finally:
    driver.quit()
