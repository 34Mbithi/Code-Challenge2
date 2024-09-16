Setup
Ensure you have Python 3.8+ installed on your system.

Clone this repository:

git clone <https://github.com/34Mbithi/Code-Challenge2/edit/master/coffee_shop>
cd coffee_shop_domain
Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required packages:

pip install pytest
Class Descriptions
Customer (customer.py)
The Customer class represents a coffee shop customer.

Attributes:

name: String, 1-15 characters long
Methods:

orders(): Returns a list of the customer's orders
coffees(): Returns a list of unique coffees the customer has ordered
create_order(coffee, price): Creates a new order for the customer
most_aficionado(coffee): Class method that returns the customer who has spent the most on a given coffee
Coffee (coffee.py)
The Coffee class represents a type of coffee available in the shop.
Attributes:

name: String, at least 3 characters long
Methods:

orders(): Returns a list of orders for this coffee
customers(): Returns a list of unique customers who have ordered this coffee
num_orders(): Returns the total number of orders for this coffee
average_price(): Returns the average price of orders for this coffee
Order (order.py)
The Order class represents an order made by a customer for a specific coffee.

Attributes:

customer: Customer instance
coffee: Coffee instance
price: Float between 1.0 and 10.0
Running the Code
To interact with the classes, you can use the debug.py script:

python debug.py
This script creates some sample customers, coffees, and orders, and demonstrates how to use various methods.

Running Tests
To run the tests, ensure you're in the project root directory and run:

pytest
This will discover and run all the tests in the tests/ directory
