from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    """Page Object для страницы калькулятора."""

    def __init__(self, driver) -> None:
        """
        Инициализация страницы калькулятора.

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CLASS_NAME, "screen")
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> 'CalculatorPage':
        """
        Открывает страницу калькулятора.

        Returns:
            CalculatorPage: текущий экземпляр страницы
        """
        self.driver.get(self.url)
        return self

    @allure.step("Установить задержку вычислений: {delay}")
    def set_delay(self, delay: int) -> 'CalculatorPage':
        """
        Устанавливает значение задержки вычислений.

        Args:
            delay: значение задержки в секундах

        Returns:
            CalculatorPage: текущий экземпляр страницы
        """
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(str(delay))
        return self

    @allure.step("Нажать кнопку: {button_text}")
    def click_button(self, button_text: str) -> 'CalculatorPage':
        """
        Нажимает указанную кнопку калькулятора.

        Args:
            button_text: текст на кнопке

        Returns:
            CalculatorPage: текущий экземпляр страницы
        """
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']"
        )
        button.click()
        return self

    @allure.step("Получить результат вычислений")
    def get_result(self, timeout: int = 50) -> str:
        """
        Получает результат вычислений с экрана калькулятора.

        Args:
            timeout: время ожидания результата

        Returns:
            str: текст результата
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(self.screen, "15"))
        return self.driver.find_element(*self.screen).text