from flask import request, jsonify

menu = {
    1: {"dish": "Pizza", "price": 800, "tasty": True},
    2: {"dish": "Burger", "price": 982, "tasty": False},
    3: {"dish": "Maggie", "price": 648, "tasty": True},
    4: {"dish": "Chowmein", "price": 242, "tasty": True},
    5: {"dish": "Pasta", "price": 752, "tasty": False},
    6: {"dish": "Dhosa", "price": 898, "tasty": True},
    7: {"dish": "French Fries", "price": 444, "tasty": True},
    8: {"dish": "Rajbhog", "price": 525, "tasty": True},
}

def read():
    return jsonify(menu), 200

def create():
    # Extract the data from the request
    data = request.get_json()
    dish = data.get("dish")
    price = data.get("price")
    tasty = data.get("tasty")

    # Find the highest key in the menu dictionary
    max_key = max(menu.keys())

    # Create a new key for the menu item
    new_key = max_key + 1

    # Add the new item to the menu
    menu[new_key] = {"dish": dish, "price": price, "tasty": tasty}

    return jsonify(menu), 201

def update(dish_id):
    # Extract the data from the request
    data = request.get_json()
    price = data.get("price")
    tasty = data.get("tasty")

    # Update the item in the menu if it exists
    if dish_id in menu:
        menu[dish_id]["price"] = price
        menu[dish_id]["tasty"] = tasty

    return jsonify(menu), 200

def delete(dish_id):
    # Delete the item from the menu if it exists
    if dish_id in menu:
        del menu[dish_id]

    return jsonify(menu), 200

def hello():
    return '<h1 style="color:blue;text-align:center">Welcome in First Flask Project API</h1>', 200

def greet(username):
    return f"Hello {username}", 200

def farewell(username):
    return f"Goodbye {username}", 200
