
# These questions simulate:

# Receiving user input

# Validating it

# Building a JSON payload

# Returning structured responses

"""🧩 Question 21: Create User Payload
📘 Problem

A user sends their name and phone number. Build a JSON payload to store the user.

📥 Input"""
name = "Lumkile"
phone = "26612345678"
# 📤 Output
{
    "user": {
        "name": "Lumkile",
        "phone": "26612345678"
    }
}
# ✅ Solution
def create_user_payload(name, phone):
    return {
        "user": {
            "name": name,
            "phone": phone
        }
    }
"""🧩 Question 22: Create Order with Total Price
📘 Problem

Given a list of products, calculate total and build payload."""

# 📥 Input
products = [
    {
     "name": "Bread", 
     "price": 10
     },
    {
      "name": "Milk", 
     "price": 15
     }
]
# 📤 Output
{
    "order": {
        "items": [...],
        "total": 25
    }
}
# ✅ Solution
def create_order(products):
    """
    Build an order payload with items and total price.
    Calculates total price step by step.
    Returns a dictionary {"order": {"items": [...], "total": total_price}}
    """
    # Initialize total price
    total_price = 0

    # Loop through each product to calculate total
    for product in products:
        # Safely get the price (default to 0 if missing)
        price = product.get("price", 0)
        # Add price to total
        total_price += price

    # Build the result dictionary
    result = {
        "order": {
            "items": products,  # Include all products as items
            "total": total_price
        }
    }

    # Return the final result
    return result
products = [
    {"name": "Bread", "price": 10},
    {"name": "Milk", "price": 15},
    {"name": "Eggs"}  # No price key, defaults to 0
]

print(create_order(products))
# Output:
# {
#     "order": {
#         "items": [
#             {"name": "Bread", "price": 10},
#             {"name": "Milk", "price": 15},
#             {"name": "Eggs"}
#         ],
#         "total": 25
#     }
# }
"""
🧩 Question 23: Add Product Quantity
📘 Problem

Each product has quantity. Calculate total cost."""

# 📥 Input
products = [
    {
        "name": "Bread", 
        "price": 10, 
        "qty": 2
        },
    {
    "name": "Milk", 
     "price": 15, 
     "qty": 1
     }
]
# 📤 Output
{
    "total": 35
}
# ✅ Solution
def calculate_total_with_quantity(products):
    """
    Calculate total cost of products considering quantity.
    Returns a dictionary {"total": total_cost}.
    """
    # Initialize total
    total_cost = 0

    # Loop through each product
    for product in products:
        # Safely get price and quantity, default to 0 if missing
        price = product.get("price", 0)
        qty = product.get("qty", 0)

        # Add price * quantity to total
        total_cost += price * qty

    # Build result dictionary
    result = {"total": total_cost}

    # Return result
    return result

products = [
    {"name": "Bread", "price": 10, "qty": 2},
    {"name": "Milk", "price": 15, "qty": 1}
]

print(calculate_total_with_quantity(products))
# Output: {"total": 35}

import requests
import json

def post_and_calculate_total(url, payload):
    """
    Post a WhatsApp webhook payload to the given URL and calculate total order cost from the response.

    Args:
        url (str): Endpoint to send POST request.
        payload (dict): WhatsApp webhook-like JSON payload.

    Returns:
        float: Total cost of all order items returned by the endpoint.
    """
    headers = {
        "Content-Type": "application/json"
    }

    try:
        # Step 1: Send POST request with the payload to the given URL
        # - `headers` specifies that we are sending JSON
        # - `json.dumps(payload)` converts the Python dict into a JSON string
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        # Step 1a: Raise an exception if the HTTP response status code indicates an error
        response.raise_for_status()  # e.g., 404, 500, or other HTTP errors

        # Step 2: Parse the JSON response from the server
        data = response.json()  # Converts JSON response into a Python dictionary

        # Step 3: Initialize total cost accumulator
        total_cost = 0

        # Step 3a: Loop through each entry in the response
        for entry in data.get("entry", []):
            # Step 3b: Loop through each change in the entry
            for change in entry.get("changes", []):
                # Step 3c: Get the 'value' dictionary which contains message info
                value = change.get("value", {})
                # Step 3d: Loop through each message in the 'messages' list
                for message in value.get("messages", []):
                    # Step 3e: Only process messages of type 'order'
                    if message.get("type") == "order":
                        # Step 3f: Access the 'order' dictionary
                        order = message.get("order", {})
                        # Step 3g: Loop through all product items in the order
                        for item in order.get("product_items", []):
                            qty = item.get("quantity", 0)      # Default to 0 if missing
                            price = item.get("item_price", 0)  # Default to 0 if missing
                            total_cost += qty * price          # Add item's total to overall total

        # Step 4: Return the calculated total cost
        return total_cost

    except requests.exceptions.RequestException as e:
        # This block runs if any network or HTTP error occurs during the POST
        print(f"Error posting payload: {e}")
        return 0  # Return 0 if POST fails or endpoint is unreachable


# Example usage
webhook_url = "https://example.com/whatsapp_webhook"  # Replace with real endpoint

payload = {
  "object": "whatsapp_business_account",
  "entry": [
    {
      "id": "WHATSAPP_BUSINESS_ACCOUNT_ID",
      "changes": [
        {
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
                "display_phone_number": "2665785555387",
                "phone_number_id": "26655656727743183882"
            },
            "contacts": [
              {
                "profile": {"name": "Lumkile Ntetha"},
                "wa_id": "26667899604"
              }
            ],
            "messages": [
              {
                "from": "26667899604",
                "id": "wamid.ID",
                "timestamp": "1518694235",
                "type": "order",
                "order": {
                  "catalog_id": "15527675282110",
                  "product_items": [
                    {"product_retailer_id": "i9sj06uvv4", "quantity": 1, "item_price": 90, "currency": "ZAR"}
                  ]
                }
              }
            ]
          },
          "field": "messages"
        }
      ]
    }
  ]
}

total = post_and_calculate_total(webhook_url, payload)
print(f"Total Order Cost: {total}")

# 🧩 Question 24: Build Chatbot Response Payload
# 📘 Problem

# User sends message → return chatbot reply JSON.

# 📥 Input
message = "Hi"
# 📤 Output
{
    "reply": {
        "text": "Hello! How can I help you?"
    }
}
# ✅ Solution
def build_chatbot_response(message):
    """
    Build a chatbot reply payload based on user message.
    Returns a dictionary with the reply text.
    """
    # For now, using a static response. Could be dynamic based on message
    reply_text = "Hello! How can I help you?"

    # Build the result dictionary
    result = {
        "reply": {
            "text": reply_text
        }
    }

    # Return the result
    return result

"""🧩 Question 25: Register User with Validation
📘 Problem

If name or phone is missing, return error JSON."""

# 📥 Input
name = ""
phone = "26612345678"

# 📤 Output
{
    "error": "Name is required"
}

# ✅ Solution
def register_user(name, phone):
    """
    Register a user with name and phone.
    Returns error JSON if required fields are missing.
    """
    # Initialize result
    result = {}

    # Validate name
    if not name:
        result = {"error": "Name is required"}
        return result  # Return immediately on error

    # Validate phone
    if not phone:
        result = {"error": "Phone is required"}
        return result  # Return immediately on error

    # If all fields are present, return success payload
    result = {
        "user": {
            "name": name,
            "phone": phone
        }
    }

    return result
name = ""
phone = "26612345678"

print(register_user(name, phone))
# Output: {"error": "Name is required"}

"""🧩 Question 26: Add Items to Cart
📘 Problem

Append new product to existing cart JSON.
"""
# 📥 Input
cart = {
    "items": [
    {
        "name": "Bread"
    }
    ]
    }
new_item = {"name": "Milk"}

# 📤 Output
{
    "items": [
        {"name": "Bread"},
        {"name": "Milk"}
    ]
}
# ✅ Solution
def add_item_to_cart(cart, new_item):
    """
    Append a new product to the existing cart.
    Returns updated cart JSON.
    """
    # Initialize result as a copy of the original cart
    result = {
        "items": cart.get("items", []).copy()  # Copy existing items safely
    }

    # Add the new item to the items list
    result["items"].append(new_item)

    return result
cart = {
    "items": [
        {"name": "Bread"}
    ]
}
new_item = {"name": "Milk"}

print(add_item_to_cart(cart, new_item))

"""🧩 Question 27: Create Invoice Payload
📘 Problem

Generate invoice JSON with subtotal and tax (10%).
"""
# 📥 Input
items = [
    {"price": 100},
    {"price": 50}
]
# 📤 Output
{
    "subtotal": 150,
    "tax": 15,
    "total": 165
}
# ✅ Solution
def create_invoice(items):
    """
    Generate invoice payload with subtotal, tax (10%), and total.
    Returns a dictionary with invoice details.
    """
    # Initialize subtotal
    subtotal = 0

    # Calculate subtotal by summing item prices
    for item in items:
        price = item.get("price", 0)  # Safely get price
        subtotal += price

    # Calculate tax (10% of subtotal)
    tax = subtotal * 0.10

    # Calculate total
    total = subtotal + tax

    # Build result dictionary
    result = {
        "subtotal": subtotal,
        "tax": tax,
        "total": total
    }

    return result
"""🧩 Question 28: Build WhatsApp Image Message Payload
📘 Problem

Create JSON to send image message.
"""
# 📥 Input
phone = "26612345678"
image_url = "http://image.com/pic.jpg"

# 📤 Output
{
    "to": "26612345678",
    "type": "image",
    "image": {
        "link": "http://image.com/pic.jpg"
    }
}

# ✅ Solution
def build_image_message(phone, image_url):
    """
    Build a WhatsApp image message payload.
    Returns a dictionary with phone, type, and image link.
    """
    # Create the payload structure
    result = {
        "to": phone,          # Recipient phone number
        "type": "image",      # Message type
        "image": {
            "link": image_url  # Image URL
        }
    }

    return result
phone = "26612345678"
image_url = "http://image.com/pic.jpg"

print(build_image_message(phone, image_url))

"""🧩 Question 29: Build Bulk Order Summary
📘 Problem

Return number of items and total quantity."""

# 📥 Input
orders = [
    {"qty": 2},
    {"qty": 3}
]

# 📤 Output
{
    "items_count": 2,
    "total_quantity": 5
}

# ✅ Solution
def build_bulk_order_summary(orders):
    """
    Return number of items and total quantity from orders.
    """
    # Count number of items (length of orders list)
    items_count = len(orders)

    # Initialize total quantity
    total_quantity = 0

    # Loop through each order to sum quantities
    for order in orders:
        qty = order.get("qty", 0)  # Safely get quantity
        total_quantity += qty

    # Build result dictionary
    result = {
        "items_count": items_count,
        "total_quantity": total_quantity
    }

    return result
orders = [
    {"qty": 2},
    {"qty": 3}
]

print(build_bulk_order_summary(orders))
"""🧩 Question 30: Create Payment Payload
📘 Problem

Generate payment request JSON."""

# 📥 Input
amount = 250
currency = "LSL"

# 📤 Output
{
    "payment": {
        "amount": 250,
        "currency": "LSL",
        "status": "pending"
    }
}

# ✅ Solution
def create_payment_payload(amount, currency):
    """
    Generate a payment request payload.
    Returns a dictionary with payment details.
    """
    # Build the result dictionary
    result = {
        "payment": {
            "amount": amount,        # Payment amount
            "currency": currency,    # Currency code (e.g., LSL)
            "status": "pending"      # Default status
        }
    }
    return result
amount = 250
currency = "LSL"

print(create_payment_payload(amount, currency))