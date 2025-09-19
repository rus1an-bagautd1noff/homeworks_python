import time
import pytest
from selenium.webdriver import Chrome
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_calculator(driver):
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
    )

    calculator = CalculatorPage(driver)

    calculator.set_delay(45)

    calculator.click_button('7')
    calculator.click_button('+')
    calculator.click_button('8')
    calculator.click_button('=')

    time.sleep(45)

    assert calculator.get_result() == '15'
