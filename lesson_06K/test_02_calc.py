import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(browser):
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    browser.get(url)

    delay_input = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.send_keys("45")

    browser.find_element(By.XPATH, "//button[text()='7']").click()
    browser.find_element(By.XPATH, "//button[text()='+']").click()
    browser.find_element(By.XPATH, "//button[text()='8']").click()
    browser.find_element(By.XPATH, "//button[text()='=']").click()

    result = WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.ID, "result"))
    )

    assert result.text == "15"
