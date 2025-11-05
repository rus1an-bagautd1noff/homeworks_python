import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.ShoppingPage import ShoppingPage


@allure.id("Internet_mag")
@allure.epic("Интернет магазин")
@allure.severity("blocker")
@allure.story("Покупка товаров")
@allure.feature("CREATE")
@allure.title("Выбор товара, работа с корзиной и оплата")
@allure.suite("Тесты на работу с интернет-магазином")
def test_form_internet_mag():
    try:
        with allure.step("Открытие веб-страницы Chrome"):
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install())
            )

        with allure.step("Создание экземпляра класса ShoppingPage"):
            internet_mag_page = ShoppingPage(driver)

        with allure.step("Авторизация пользователя"):
            internet_mag_page.authorization("standard_user", "secret_sauce")

        with allure.step("Добавление товаров в корзину"):
            to_be = internet_mag_page.add_products()

        with allure.step("Переход в корзину"):
            internet_mag_page.go_to_cart()

        with allure.step("Заполнение данных пользователя"):
            internet_mag_page.personal_data(
                "Svetlana", "Voroshilova", "420105"
            )

        with allure.step("Получение итоговой стоимости"):
            as_is = internet_mag_page.total_cost()

        with allure.step("Проверка совпадения стоимости"):
            assert as_is == to_be, (
                f"Ожидаемая стоимость: {to_be}, "
                f"фактическая: {as_is}"
            )

    finally:
        with allure.step("Закрытие браузера"):
            internet_mag_page.close()
