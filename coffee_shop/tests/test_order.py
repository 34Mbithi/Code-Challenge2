import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_creation():
    c = Customer("John")
    coffee = Coffee("Espresso")
    order = Order(c, coffee, 5.0)
    assert order.price == 5.0
    with pytest.raises(ValueError):
        Order(c, coffee, 0.5)
