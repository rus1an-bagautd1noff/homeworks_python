from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")

    input_field = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "inputValue"))
    )

    input_field.send_keys("SkyPro")

    button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()

    updated_button_text = WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "button.btn-primary"),
            "SkyPro"
        )
    )

    print(button.text)

finally:
    driver.quit()
