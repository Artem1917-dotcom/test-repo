from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.CLASS_NAME, "radius")

username_field.send_keys("tomsmith")
password_field.send_keys("SuperSecretPassword!")
login_button.click()

success_message = driver.find_element(By.CLASS_NAME, "success")
print(success_message.text)

driver.quit()