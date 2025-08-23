from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/dynamicid")

    wait = WebDriverWait(driver, 5)

    blue_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Click me']"))
    )

    blue_button.click()

    time.sleep(3)

finally:
    driver.quit()
