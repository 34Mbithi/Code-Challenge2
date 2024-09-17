from customer import Customer
from coffee import Coffee



class Order:
    _all = []  # Class-level list to store all order instances

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order._all.append(self)

    # Property for customer with validation
    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise ValueError("Order must have a valid Customer instance.")
        self._customer = value

    # Property for coffee with validation
    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise ValueError("Order must have a valid Coffee instance.")
        self._coffee = value

    # Property for price with validation
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not (1.0 <= value <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")
        self._price = value
