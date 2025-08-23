from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/login")
    driver.maximize_window()
    
    wait = WebDriverWait(driver, 10)
    
    username_field = wait.until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_field.send_keys("tomsmith")
    
    password_field = wait.until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_field.send_keys("SuperSecretPassword!")
    
    login_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#login > button"))
    )
    login_button.click()
    
    success_message = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
    )
    print("Сообщение об успехе:", success_message.text)
    
    time.sleep(2)
    
finally:
    driver.quit()
