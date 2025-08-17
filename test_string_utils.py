import pytest
from string_utils import StringUtils

class TestStringUtils:
    # Тесты для capitalize_string
    def test_capitalize_positive(self):
        assert StringUtils.capitalize_string("тест") == "Тест"
        assert StringUtils.capitalize_string("тест строка") == "Тест строка"
    
    def test_capitalize_negative(self):
        assert StringUtils.capitalize_string("") == ""
        assert StringUtils.capitalize_string(" ") == " "
        with pytest.raises(ValueError):
            StringUtils.capitalize_string(None)

    # Тесты для trim_string
    def test_trim_positive(self):
        assert StringUtils.trim_string("  тест") == "тест"
        assert StringUtils.trim_string(" тест ") == "тест "
    
    def test_trim_negative(self):
        assert StringUtils.trim_string("") == ""
        with pytest.raises(ValueError):
            StringUtils.trim_string(123)

    # Тесты для to_list
    def test_to_list_positive(self):
        assert StringUtils.to_list("1,2,3") == ["1", "2", "3"]
        assert StringUtils.to_list("a|b|c", "|") == ["a", "b", "c"]
    
    def test_to_list_negative(self):
        assert StringUtils.to_list("") == []
        with pytest.raises(ValueError):
            StringUtils.to_list(123, ",")
        with pytest.raises(ValueError):
            StringUtils.to_list("1,2,3", 123)

    # Тесты для contains
    def test_contains_positive(self):
        assert StringUtils.contains("тест", "е") is True
        assert StringUtils.contains("строка", "рок") is True
    
    def test_contains_negative(self):
        assert StringUtils.contains("тест", "z") is False
        with pytest.raises(ValueError):
            StringUtils.contains(123, "1")
        with pytest.raises(ValueError):
            StringUtils.contains("тест", 1)