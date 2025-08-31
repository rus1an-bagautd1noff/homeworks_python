from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located(
            (By.TAG_NAME, "img")
        )
    )

    images = driver.find_elements(By.TAG_NAME, "img")

    if len(images) >= 3:
        third_image_src = images[2].get_attribute("src")
        print(
            f"Src третьей картинки: {third_image_src}"
        )
    else:
        print("На странице меньше трех изображений")

finally:
    driver.quit()
