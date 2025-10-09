# lesson_10/tests/test_steps.py
import allure


@allure.feature("Авторизация")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Тест входа в систему")
@allure.description("Проверка успешного входа пользователя")
def test_login():
    with allure.step("Открываем страницу входа"):
        # Здесь должен быть код открытия страницы
        pass

    @allure.step("Ввод данных")
    def enter_credentials():
        # Здесь код ввода данных
        pass

    with allure.step("Проверка результата"):
        # Здесь проверка результата
        assert True  # Пример проверки
