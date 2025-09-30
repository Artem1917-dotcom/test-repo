from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:
    """Page Object для страницы оформления заказа."""

    def __init__(self, driver) -> None:
        """
        Инициализация страницы оформления заказа.

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнить информацию для оформления заказа")
    def fill_checkout_info(
        self, first_name: str, last_name: str, postal_code: str
    ) -> 'CheckoutPage':
        """
        Заполняет информацию для оформления заказа.

        Args:
            first_name: имя
            last_name: фамилия
            postal_code: почтовый индекс

        Returns:
            CheckoutPage: текущий экземпляр страницы
        """
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()
        return self

    @allure.step("Получить итоговую сумму заказа")
    def get_total_amount(self) -> str:
        """
        Получает итоговую сумму заказа.

        Returns:
            str: текст итоговой суммы
        """
        wait = WebDriverWait(self.driver, 10)
        total_element = wait.until(
            EC.visibility_of_element_located(self.total_label)
        )
        return total_element.text