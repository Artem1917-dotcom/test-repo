import pytest
from string_utils import StringUtils

class TestStringUtils:
    utils = StringUtils()

    # Позитивные тесты
    def test_capitalize_positive(self):
        assert self.utils.capitalize("skypro") == "Skypro"
    
    def test_trim_positive(self):
        assert self.utils.trim("   skypro") == "skypro"
    
    def test_contains_positive(self):
        assert self.utils.contains("SkyPro", "S") is True
    
    def test_delete_symbol_positive(self):
        assert self.utils.delete_symbol("SkyPro", "k") == "SyPro"

    # Негативные тесты
    def test_capitalize_negative(self):
        assert self.utils.capitalize("") == ""
    
    def test_trim_negative(self):
        assert self.utils.trim("") == ""
    
    def test_contains_negative(self):
        assert self.utils.contains("SkyPro", "U") is False
    
    def test_delete_symbol_negative(self):
        assert self.utils.delete_symbol("", "a") == ""