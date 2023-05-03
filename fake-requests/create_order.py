import requests
import json

# Define the API URL
api_url = "http://localhost:8000/orders"

# Define the order data
order = {
    "customer_name": "John Doe",
    "pizza_type": "Pepperoni",
    "size": "Medium",
    "toppings": ["Mushrooms", "Onions"]
}

# Send a POST request to create the order
response = requests.post(api_url, json=order)

# Check the response status code
if response.status_code == 200:
    print("Order created successfully!")
else:
    print("Error creating order.")
