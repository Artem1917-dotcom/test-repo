from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")

blue_button = driver.find_element(By.ID, "updatingButton")
blue_button.click()

wait = WebDriverWait(driver, 10)
updated_button = wait.until(
    EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
)

blue_button_text = driver.find_element(By.ID, "updatingButton").text
print(blue_button_text)

driver.quit()