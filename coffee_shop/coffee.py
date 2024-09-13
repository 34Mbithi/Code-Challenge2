class Coffee:
    _all = []  # Class-level list to store all coffee instances

    def __init__(self, name):
        self.name = name
        self._orders = []  # Stores all orders associated with this coffee
        Coffee._all.append(self)

    # Property for 'name' with validation
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Coffee name must be a string.")
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
        self._name = value

    # Method to return all orders associated with the coffee
    def orders(self):
        return self._orders

    # Method to return all unique customers who ordered the coffee
    def customers(self):
        return list(set([order.customer for order in self._orders]))

    # Method to return the number of orders for the coffee
    def num_orders(self):
        return len(self._orders)

    # Method to return the average price of the coffee
    def average_price(self):
        if not self._orders:
            return 0
        total_price = sum([order.price for order in self._orders])
        return total_price / len(self._orders)
