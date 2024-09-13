Setup
Ensure you have Python 3.8+ installed on your system.

Clone this repository:

git clone <repository-url>
cd coffee_shop_domain
(Optional) Create and activate a virtual environment:

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
This will discover and run all the tests in the tests/ directory.

Logic Behind Classes and Attributes
Encapsulation: Each class encapsulates its data (attributes) and behaviors (methods). For example, the Customer class encapsulates the customer's name and their orders.

Data Validation: Setters are used to validate data before assigning it to attributes. For instance, the name setter in both Customer and Coffee classes ensures the name meets specific criteria.

Relationships:

A Customer can have many Orders (one-to-many)
A Coffee can have many Orders (one-to-many)
An Order belongs to one Customer and one Coffee (many-to-one for both)
Aggregation Methods: Methods like num_orders() and average_price() in the Coffee class provide aggregate information about the orders.

Unique Collections: Methods like coffees() in Customer and customers() in Coffee return unique collections, implemented using sets.

Class Methods: The most_aficionado() method in Customer is a class method, as it operates on the class level rather than on a specific instance.

Bidirectional Relationships: When an Order is created, it's added to both the Customer's and Coffee's order lists, maintaining the bidirectional relationship.

This project demonstrates key OOP concepts including encapsulation, data validation, class relationships, and method design. It provides a foundation that can be extended for more complex coffee shop operations.
