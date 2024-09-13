class Customer:
    _all = []  # Class-level list to store all customer instances

    def __init__(self, name):
        self.name = name
        self._orders = []  # Stores all orders associated with this customer
        Customer._all.append(self)

    # Property for 'name' with validation
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Customer name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters.")
        self._name = value

    # Method to return all orders associated with the customer
    def orders(self):
        return self._orders

    # Method to return all unique coffees that the customer has ordered
    def coffees(self):
        return list(set([order.coffee for order in self._orders]))

    # Method to create a new order for the customer
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        coffee._orders.append(new_order)

    @classmethod
    def most_aficionado(cls, coffee):
        customer_spending = {}
        for order in coffee.orders():
            customer = order.customer
            if customer not in customer_spending:
                customer_spending[customer] = 0
            customer_spending[customer] += order.price
        return max(customer_spending, key=customer_spending.get, default=None)
