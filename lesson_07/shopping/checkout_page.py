from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.total_amount = (By.CSS_SELECTOR, "#total_amount")

    def fill_first_name(self, first_name):
        self.driver.find_element(*self.first_name).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.driver.find_element(*self.last_name).send_keys(last_name)

    def fill_postal_code(self, postal_code):
        self.driver.find_element(*self.postal_code).send_keys(postal_code)

    def get_total_amount(self):
        return self.driver.find_element(*self.total_amount).text
