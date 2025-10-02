from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CLASS_NAME, "screen")
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def open(self):
        self.driver.get(self.url)
        return self

    def set_delay(self, delay):
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(str(delay))
        return self

    def click_button(self, button_text):
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']")
        button.click()
        return self

    def get_result(self, timeout=50):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(self.screen, "15"))
        return self.driver.find_element(*self.screen).text
