from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ждем, пока все картинки загрузятся (пока не исчезнет спиннер загрузки)
wait = WebDriverWait(driver, 15)
wait.until(
    EC.invisibility_of_element_located((By.ID, "spinner"))
)

# Ждем, пока появится хотя бы 4 картинки (включая третью)
wait.until(
    lambda driver: len(driver.find_elements(By.CSS_SELECTOR, "#image-container img")) >= 4
)

# Получаем третью картинку
all_images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
third_image = all_images[2]  # третья картинка имеет индекс 2

# Получаем значение атрибута src
src_attribute = third_image.get_attribute("src")
print(src_attribute)

driver.quit()