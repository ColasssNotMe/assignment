# use products.txt to store product data
# use orders.txt to store customer order data
# Define the file to store data
# if using this file, do "from inventory_system import menu"
# make a "inventory" option from admin / superuser menu
## no global variable
def initialize_data():
    try:
        with open("INVENTORY_DATA.TXT", "x") as f:
            f.write("Inventory:\n")
            f.write("Purchase Orders:\n")
    except FileExistsError:
        pass


def save_data(inventory, purchase_orders):
    with open("INVENTORY_DATA.TXT", "w") as f:
        f.write("Inventory:\n")
        for item, quantity in inventory.items():
            f.write(f"{item}: {quantity}\n")
        f.write("Purchase Orders:\n")
        for order_id, order_details in purchase_orders.items():
            item_name = order_details["item_name"]
            quantity = order_details["quantity"]
            status = order_details["status"]
            f.write(f"{order_id}: {item_name}, {quantity}, {status}\n")


def load_data():
    inventory = {}
    purchase_orders = {}
    with open("INVENTORY_DATA.TXT", "r") as f:
        lines = f.readlines()
        section = None
        for line in lines:
            line = line.strip()
            if line == "Inventory:":
                section = "inventory"
            elif line == "Purchase Orders:":
                section = "purchase_orders"
            elif line and section == "inventory":
                item, quantity = line.split(": ")
                inventory[item] = int(quantity)
            elif line and section == "purchase_orders":
                order_id, details = line.split(": ")
                item_name, quantity, status = details.split(", ")
                purchase_orders[order_id] = {
                    "item_name": item_name,
                    "quantity": int(quantity),
                    "status": status,
                }
    return inventory, purchase_orders


def add_or_update_inventory(item_name, quantity):
    inventory, purchase_orders = load_data()
    inventory[item_name] = inventory.get(item_name, 0) + quantity
    save_data(inventory, purchase_orders)


def check_stock(item_name):
    inventory, _ = load_data()
    return inventory.get(item_name, 0)


def adjust_stock(item_name, quantity):
    inventory, purchase_orders = load_data()
    if item_name in inventory:
        inventory[item_name] += quantity
        if inventory[item_name] < 0:
            inventory[item_name] = 0
        save_data(inventory, purchase_orders)
    else:
        print("Item not found in inventory.")


def create_purchase_order(order_id, item_name, quantity):
    inventory, purchase_orders = load_data()
    if item_name in inventory:
        purchase_orders[order_id] = {
            "item_name": item_name,
            "quantity": quantity,
            "status": "in process",
        }
        save_data(inventory, purchase_orders)
    else:
        print("Item not found in inventory.")


def modify_purchase_order(order_id, new_item_name=None, new_quantity=None):
    inventory, purchase_orders = load_data()
    if order_id in purchase_orders:
        if new_item_name:
            purchase_orders[order_id]["item_name"] = new_item_name
        if new_quantity is not None:
            purchase_orders[order_id]["quantity"] = new_quantity
        save_data(inventory, purchase_orders)
    else:
        print("Order ID not found.")


def cancel_purchase_order(order_id):
    inventory, purchase_orders = load_data()
    if order_id in purchase_orders:
        del purchase_orders[order_id]
        save_data(inventory, purchase_orders)
    else:
        print("Order ID not found.")


def get_order_status(order_id):
    _, purchase_orders = load_data()
    return purchase_orders.get(order_id, {}).get("status", "Order ID not found.")


def generate_report():
    inventory, purchase_orders = load_data()
    print("Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")
    print("\nPurchase Orders:")
    for order_id, order_details in purchase_orders.items():
        item_name = order_details["item_name"]
        quantity = order_details["quantity"]
        status = order_details["status"]
        print(f"{order_id}: {item_name}, {quantity}, {status}")


def menu():
    initialize_data()
    while True:
        print("\nInventory Management System")
        print("1. Add/Update Inventory Item")
        print("2. Check Stock")
        print("3. Adjust Stock")
        print("4. Create Purchase Order")
        print("5. Modify Purchase Order")
        print("6. Cancel Purchase Order")
        print("7. Get Purchase Order Status")
        print("8. Generate Report")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_or_update_inventory(item_name, quantity)
        elif choice == "2":
            item_name = input("Enter item name: ")
            print(f"Stock for {item_name}: {check_stock(item_name)}")
        elif choice == "3":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity adjustment (positive or negative): "))
            adjust_stock(item_name, quantity)
        elif choice == "4":
            order_id = input("Enter order ID: ")
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            create_purchase_order(order_id, item_name, quantity)
        elif choice == "5":
            order_id = input("Enter order ID: ")
            new_item_name = input(
                "Enter new item name (or leave blank to keep current): "
            )
            new_quantity = input(
                "Enter new quantity (or leave blank to keep current): "
            )
            new_quantity = int(new_quantity) if new_quantity else None
            modify_purchase_order(
                order_id, new_item_name if new_item_name else None, new_quantity
            )
        elif choice == "6":
            order_id = input("Enter order ID: ")
            cancel_purchase_order(order_id)
        elif choice == "7":
            order_id = input("Enter order ID: ")
            print(f"Status for order ID {order_id}: {get_order_status(order_id)}")
        elif choice == "8":
            generate_report()
        elif choice == "9":
            break
        else:
            print("Invalid choice, please try again.")
