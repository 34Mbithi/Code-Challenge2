import pytest
from coffee import Coffee

def test_coffee_creation():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"
    with pytest.raises(ValueError):
        Coffee("Te")
