from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

# Нажимаем на синюю кнопку
blue_button = driver.find_element(By.ID, "ajaxButton")
blue_button.click()

# Ждем, пока появится элемент с конкретным текстом
wait = WebDriverWait(driver, 15)
success_message = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'bg-success') and contains(text(), 'Data loaded')]"))
)

# Получаем и выводим текст
print(success_message.text)

driver.quit()