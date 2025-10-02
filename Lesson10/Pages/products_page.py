from selenium.webdriver.common.by import By
from .cart_page import CartPage
import allure


class ProductsPage:
    """Page Object для страницы продуктов."""

    def __init__(self, driver) -> None:
        """
        Инициализация страницы продуктов.

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавить продукт в корзину: {product_id}")
    def add_product_to_cart(self, product_id: str) -> 'ProductsPage':
        """
        Добавляет продукт в корзину.

        Args:
            product_id: идентификатор продукта

        Returns:
            ProductsPage: текущий экземпляр страницы
        """
        add_button = self.driver.find_element(
            By.ID, f"add-to-cart-{product_id}"
        )
        add_button.click()
        return self

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> CartPage:
        """
        Переходит на страницу корзины.

        Returns:
            CartPage: экземпляр страницы корзины
        """
        self.driver.find_element(*self.cart_link).click()
        return CartPage(self.driver)
