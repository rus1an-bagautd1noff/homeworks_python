import allure
from pages.page import Page


@allure.feature("Проверка главной страницы")
@allure.severity(allure.severity_level.BLOCKER)
class TestMainPage:
    @allure.title("Тест открытия главной страницы")
    @allure.description("Проверка корректности открытия главной страницы")
    def test_open_main_page(self, driver):
        with allure.step("Открываем главную страницу"):
            page = Page(driver)
            page.open("https://example.com")

        with allure.step("Проверяем заголовок страницы"):
            assert page.get_title() == "Expected Title"
