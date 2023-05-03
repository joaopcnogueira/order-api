import requests

api_url = "http://localhost:8000/orders"

# Define a list of 10 orders to create
orders = [
    {
        "customer_name": "Alice",
        "pizza_type": "Margherita",
        "size": "Medium",
        "toppings": ["Tomatoes", "Basil", "Mozzarella"]
    },
    {
        "customer_name": "Bob",
        "pizza_type": "Pepperoni",
        "size": "Large",
        "toppings": ["Pepperoni", "Mushrooms", "Onions", "Extra Cheese"]
    },
    {
        "customer_name": "Charlie",
        "pizza_type": "Vegetarian",
        "size": "Small",
        "toppings": ["Tomatoes", "Mushrooms", "Onions", "Peppers", "Olives", "Feta Cheese"]
    },
    {
        "customer_name": "Dave",
        "pizza_type": "Hawaiian",
        "size": "Medium",
        "toppings": ["Pineapple", "Ham", "Mozzarella"]
    },
    {
        "customer_name": "Eve",
        "pizza_type": "Meat Lovers",
        "size": "Large",
        "toppings": ["Pepperoni", "Sausage", "Bacon", "Ham", "Mozzarella"]
    },
    {
        "customer_name": "Frank",
        "pizza_type": "Supreme",
        "size": "Medium",
        "toppings": ["Pepperoni", "Sausage", "Onions", "Peppers", "Mushrooms", "Olives", "Mozzarella"]
    },
    {
        "customer_name": "Grace",
        "pizza_type": "Margherita",
        "size": "Small",
        "toppings": ["Tomatoes", "Basil", "Mozzarella"]
    },
    {
        "customer_name": "Henry",
        "pizza_type": "Pepperoni",
        "size": "Medium",
        "toppings": ["Pepperoni", "Mozzarella"]
    },
    {
        "customer_name": "Isabelle",
        "pizza_type": "Hawaiian",
        "size": "Large",
        "toppings": ["Pineapple", "Ham", "Bacon", "Mozzarella"]
    },
    {
        "customer_name": "Jack",
        "pizza_type": "Veggie",
        "size": "Medium",
        "toppings": ["Tomatoes", "Mushrooms", "Onions", "Peppers", "Olives", "Mozzarella"]
    }
]

# Loop through the orders and create them using the API
for order in orders:
    response = requests.post(api_url, json=order)
    print(response.json())
