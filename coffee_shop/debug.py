from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
john = Customer("John")
jane = Customer("Jane")

# Create coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create orders
john.create_order(latte, 5.5)
john.create_order(espresso, 4.0)
jane.create_order(latte, 6.0)

# Check order details
print(f"{john.name} ordered {john.coffees()}")
print(f"{latte.name} has {latte.num_orders()} orders with average price {latte.average_price()}")


print(Customer.most_aficionado(latte))  # Outputs Customer object who spent the most
