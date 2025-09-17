import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def browser():
    service = Service(GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shopping_cart(browser):
    url = "https://www.saucedemo.com/"
    browser.get(url)

    username = browser.find_element(By.ID, "user-name")
    password = browser.find_element(By.ID, "password")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_item"))
    )

    backpack_xpath = (
        "//divcontains(text(), 'Backpack')"
        "/following-sibling::button"
    )
    browser.find_element(By.XPATH, backpack_xpath).click()

    t_shirt_xpath = (
        "//divcontains(text(), 'Bolt T-Shirt')"
        "/following-sibling::button"
    )
    browser.find_element(By.XPATH, t_shirt_xpath).click()

    onesie_xpath = (
        "//divcontains(text(), 'Onesie')"
        "/following-sibling::button"
    )
    browser.find_element(By.XPATH, onesie_xpath).click()

    browser.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    browser.find_element(By.CSS_SELECTOR, ".checkout-button").click()

    first_name = browser.find_element(By.ID, "first-name")
    last_name = browser.find_element(By.ID, "last-name")
    postal_code = browser.find_element(By.ID, "postal-code")

    first_name.send_keys("Иван")
    last_name.save_keys("Петров")
    postal_code.send_keys("12345")

    browser.find_element(By.ID, "continue").click()

    total_amount = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR,
            ".summary_total_value"
        ))
    )

    assert total_amount.text == "$58.29"
