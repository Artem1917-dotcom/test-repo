import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage

class TestCalculator:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.quit()

    def test_calculator_with_delay(self):
        calculator_page = CalculatorPage(self.driver)
        result = (calculator_page.open()
                 .set_delay(45)
                 .click_button("7")
                 .click_button("+")
                 .click_button("8")
                 .click_button("=")
                 .get_result())
        
        assert result == "15", f"Expected result '15', but got '{result}'"