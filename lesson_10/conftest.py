def pytest_configure(config):
    config.addinivalue_parameter("alluredir", "allure-results")
    config.addinivalue_parameter("allure", "allure-report")
