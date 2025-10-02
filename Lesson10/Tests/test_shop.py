from Pages.login_page import LoginPage
import pytest
import sys
import os
from selenium import webdriver

# Добавляем путь к корневой папке проекта
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


try:
    import allure
except ImportError:
    # Fallback if allure is not installed
    class AllureDummy:
        def step(self, *args, **kwargs):
            return lambda func: func

        def title(self, title):
            return lambda func: func

        def description(self, description):
            return lambda func: func

        def feature(self, feature):
            return lambda func: func

        def severity(self, severity):
            return lambda func: func
        severity_level = type('obj', (object,), {
            'CRITICAL': 'critical'
        })
    allure = AllureDummy()


class TestShop:
    """Тесты для интернет-магазина."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Настройка тестового окружения."""
        self.driver = webdriver.Firefox()
        yield
        self.driver.quit()

    @allure.title("Тест корзины интернет-магазина")
    @allure.description("Проверка итоговой суммы заказа в корзине интернет-магазина")
    @allure.feature("Shopping Cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_shopping_cart_total(self):
        """Тестирование итоговой суммы заказа."""
        with allure.step("Авторизоваться как стандартный пользователь"):
            products_page = (LoginPage(self.driver)
                             .open()
                             .login("standard_user", "secret_sauce"))

        with allure.step("Добавить товары в корзину"):
            (products_page.add_product_to_cart("sauce-labs-backpack")
             .add_product_to_cart("sauce-labs-bolt-t-shirt")
             .add_product_to_cart("sauce-labs-onesie"))

        with allure.step("Перейти к оформлению заказа"):
            cart_page = products_page.go_to_cart()
            checkout_page = cart_page.checkout()

        with allure.step("Заполнить информацию для доставки"):
            total_text = (checkout_page.fill_checkout_info("Иван", "Петров", "123456")
                          .get_total_amount())

        with allure.step("Проверить итоговую сумму"):
            assert total_text == "Total: $58.29", (
                f"Expected 'Total: $58.29', but got '{total_text}'"
            )
