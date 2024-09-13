import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_creation():
    c = Customer("John")
    assert c.name == "John"
    with pytest.raises(ValueError):
        Customer("This name is too long")
