import json


def set_orders(orders: dict):
    while True:
        name = input("Enter your name: ")
        if not name:
            break

        orders[name] = input("Enter your order: ")

    with open("order_file.json", "w") as file:
        json.dump(orders, file)


def get_orders():
    try:
        with open("order_file.json", "r") as file:
            orders = json.load(file)

        return orders
    except:
        raise Exception("There no orders")


orders = {}

set_orders(orders)

orders = get_orders()

print(orders)