from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")

    button = driver.find_element(
        By.CSS_SELECTOR,
        "button.btn-primary"
    )
    button.click()

    message = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.alert.alert-success")
        )
    )

    print(message.text)

finally:
    driver.quit()
