from selenium.webdriver.common.by import By
from .products_page import ProductsPage
import allure


class LoginPage:
    """Page Object для страницы авторизации."""

    def __init__(self, driver) -> None:
        """
        Инициализация страницы авторизации.

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.url = "https://www.saucedemo.com/"

    @allure.step("Открыть страницу авторизации")
    def open(self) -> 'LoginPage':
        """
        Открывает страницу авторизации.

        Returns:
            LoginPage: текущий экземпляр страницы
        """
        self.driver.get(self.url)
        return self

    @allure.step("Выполнить авторизацию пользователем: {username}")
    def login(self, username: str, password: str) -> ProductsPage:
        """
        Выполняет авторизацию пользователя.

        Args:
            username: имя пользователя
            password: пароль

        Returns:
            ProductsPage: экземпляр страницы продуктов
        """
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        return ProductsPage(self.driver)