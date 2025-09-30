from selenium.webdriver.common.by import By
from .checkout_page import CheckoutPage
import allure


class CartPage:
    """Page Object для страницы корзины."""

    def __init__(self, driver) -> None:
        """
        Инициализация страницы корзины.

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    @allure.step("Начать оформление заказа")
    def checkout(self) -> CheckoutPage:
        """
        Начинает процесс оформления заказа.

        Returns:
            CheckoutPage: экземпляр страницы оформления заказа
        """
        self.driver.find_element(*self.checkout_button).click()
        return CheckoutPage(self.driver)