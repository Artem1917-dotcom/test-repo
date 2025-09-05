import pytest
from selenium import webdriver
from pages.login_page import LoginPage

class TestShop:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.quit()

    def test_shopping_cart_total(self):
        products_page = (LoginPage(self.driver)
                        .open()
                        .login("standard_user", "secret_sauce"))
        
        (products_page.add_product_to_cart("sauce-labs-backpack")
         .add_product_to_cart("sauce-labs-bolt-t-shirt")
         .add_product_to_cart("sauce-labs-onesie"))
        
        cart_page = products_page.go_to_cart()
        checkout_page = cart_page.checkout()
        
        total_text = (checkout_page.fill_checkout_info("Иван", "Петров", "123456")
                     .get_total_amount())
        
        assert total_text == "Total: $58.29", f"Expected 'Total: $58.29', but got '{total_text}'"