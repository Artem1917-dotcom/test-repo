import pytest
import sys
import os
from selenium import webdriver

# Добавляем путь к корневой папке проекта
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Pages.calculator_page import CalculatorPage

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


class TestCalculator:
    """Тесты для калькулятора."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Настройка тестового окружения."""
        self.driver = webdriver.Chrome()
        yield
        self.driver.quit()

    @allure.title("Тест калькулятора с задержкой")
    @allure.description("Проверка работы калькулятора с установленной задержкой вычислений")
    @allure.feature("Calculator")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_calculator_with_delay(self):
        """Тестирование калькулятора с задержкой вычислений."""
        calculator_page = CalculatorPage(self.driver)
        
        with allure.step("Выполнить операцию 7 + 8 с задержкой 45 секунд"):
            result = (calculator_page.open()
                     .set_delay(45)
                     .click_button("7")
                     .click_button("+")
                     .click_button("8")
                     .click_button("=")
                     .get_result())
        
        with allure.step("Проверить что результат равен 15"):
            assert result == "15", f"Expected result '15', but got '{result}'"