import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture
def browser():
    service = EdgeService(EdgeChromiumDriverManager().install())
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_validation(browser):
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    browser.get(url)

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "firstname"))
    )

    browser.find_element(By.NAME, "firstname").send_keys("Иван")
    browser.find_element(By.NAME, "lastname").send_keys("Петров")
    browser.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    browser.find_element(By.NAME, "email").send_keys("test@skypro.com")
    browser.find_element(By.NAME, "phone").send_keys("+7985899998787")
    browser.find_element(By.NAME, "city").send_keys("Москва")
    browser.find_element(By.NAME, "country").send_keys("Россия")
    browser.find_element(By.NAME, "position").send_keys("QA")
    browser.find_element(By.NAME, "company").send_keys("SkyPro")

    browser.find_element(By.NAME, "submit").click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".form-control"))
    )

    fields = browser.find_elements(By.CSS_SELECTOR, ".form-control")

    for field in fields:
        field_name = field.get_attribute("name")
        if field_name == "zip":
            assert "is-invalid" in field.get_attribute("class")
        else:
            assert "is-valid" in field.get_attribute("class")
