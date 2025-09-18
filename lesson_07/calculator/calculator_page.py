from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.delay_field = (By.CSS_SELECTOR, '#delay')
        self.result_field = (By.CSS_SELECTOR, '#result')
        self.buttons = {
            '7': (By.XPATH, '//button[text()="7"]'),
            '+': (By.XPATH, '//button[text()="+"]'),
            '8': (By.XPATH, '//button[text()="8"]'),
            '=': (By.XPATH, '//button[text()="="]')
        }

    def set_delay(self, delay: int):
        self.driver.find_element(*self.delay_field).clear()
        self.driver.find_element(*self.delay_field).send_keys(str(delay))

    def click_button(self, button: str):
        self.driver.find_element(*self.buttons[button]).click()

    def get_result(self) -> str:
        return self.driver.find_element(*self.result_field).text
