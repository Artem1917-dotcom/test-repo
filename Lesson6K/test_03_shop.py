from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shopping_cart_total():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавляем товары в корзину
    wait = WebDriverWait(driver, 10)

    # Sauce Labs Backpack
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Sauce Labs Bolt T-Shirt
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    # Sauce Labs Onesie
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Нажимаем Checkout
    driver.find_element(By.ID, "checkout").click()

    # Заполняем форму
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    # Читаем итоговую стоимость
    total_element = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text

    # Проверяем итоговую сумму
    assert total_text == "Total: $58.29"

    driver.quit()
