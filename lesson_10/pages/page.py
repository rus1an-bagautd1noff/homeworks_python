class Page:
    """
    Базовый класс для работы со страницами
    """

    def __init__(self, driver):
        """
        Инициализация страницы

        :param driver: WebDriver объект
        """
        self.driver = driver

    def open(self, url: str) -> None:
        """
        Открытие страницы по URL

        :param url: URL страницы
        """
        self.driver.get(url)

    def get_title(self) -> str:
        """
        Получение заголовка страницы

        :return: Заголовок страницы
        """
        return self.driver.title
