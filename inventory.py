from User_Management import write_user_usage


def initialize_data():
    try:
        with open("INVENTORY_DATA.TXT", "x") as f:
            f.write("Inventory:\n")
            f.write("Purchase Orders:\n")
    except FileExistsError:
        pass


def save_data(inventory, purchase_orders, prices):
    with open("INVENTORY_DATA.TXT", "w") as f:
        f.write("Inventory:\n")
        for item, quantity in inventory.items():
            price = prices.get(item, 0)
            f.write(f"{item}: {quantity}: {price}\n")
        f.write("Purchase Orders:\n")
        for order_id, order_details in purchase_orders.items():
            item_name = order_details["item_name"]
            quantity = order_details["quantity"]
            price = order_details["price"]
            status = order_details["status"]
            f.write(f"{order_id}: {item_name}, {quantity}, {price}, {status}\n")


def load_data():
    inventory = {}
    purchase_orders = {}
    prices = {}
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
                item, quantity_price = line.split(": ", 1)
                quantity, price = quantity_price.split(": ")
                inventory[item.strip()] = int(quantity.strip())
                prices[item.strip()] = int(price.strip())
            elif line and section == "purchase_orders":
                order_id, details = line.split(": ")
                item_name, quantity, price, status = details.split(", ")
                purchase_orders[order_id] = {
                    "item_name": item_name,
                    "quantity": int(quantity),
                    "price": int(price),
                    "status": status,
                }
    return inventory, purchase_orders, prices


def add_or_update_inventory(item_name, quantity, price):
    inventory, purchase_orders, prices = load_data()
    inventory[item_name] = quantity
    prices[item_name] = price
    save_data(inventory, purchase_orders, prices)


def check_stock(item_name):
    inventory, _, _ = load_data()
    return inventory.get(item_name, 0)


def adjust_stock(item_name, quantity):
    inventory, purchase_orders, prices = load_data()
    if item_name in inventory:
        inventory[item_name] += quantity
        if inventory[item_name] < 0:
            inventory[item_name] = 0
        save_data(inventory, purchase_orders, prices)
    else:
        print("Item not found in inventory.")


def create_purchase_order(order_id, item_name, quantity, price):
    inventory, purchase_orders, prices = load_data()
    if item_name in inventory:
        purchase_orders[order_id] = {
            "item_name": item_name,
            "quantity": quantity,
            "price": price,
            "status": "in process",
        }
        save_data(inventory, purchase_orders, prices)
    else:
        print("Item not found in inventory.")


def modify_purchase_order(order_id, new_item_name=None, new_quantity=None):
    inventory, purchase_orders, prices = load_data()
    if order_id in purchase_orders:
        if new_item_name:
            purchase_orders[order_id]["item_name"] = new_item_name
        if new_quantity is not None:
            purchase_orders[order_id]["quantity"] = new_quantity
        save_data(inventory, purchase_orders, prices)
    else:
        print("Order ID not found.")


def cancel_purchase_order(order_id):
    inventory, purchase_orders, prices = load_data()
    if order_id in purchase_orders:
        del purchase_orders[order_id]
        save_data(inventory, purchase_orders, prices)
    else:
        print("Order ID not found.")


def get_order_status(order_id):
    _, purchase_orders, _ = load_data()
    return purchase_orders.get(order_id, {}).get("status", "Order ID not found.")


def generate_report():
    inventory, purchase_orders, prices = load_data()
    print("Inventory:")
    for item, quantity in inventory.items():
        price = prices.get(item, 0)
        print(f"{item}: {quantity} (Price: {price})")
    print("\nPurchase Orders:")
    for order_id, order_details in purchase_orders.items():
        item_name = order_details["item_name"]
        quantity = order_details["quantity"]
        price = order_details["price"]
        status = order_details["status"]
        print(f"{order_id}: {item_name}, {quantity}, {price}, {status}")


def menu(current_user):
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
            price = int(input("Enter price: "))
            add_or_update_inventory(item_name, quantity, price)
            write_user_usage(
                current_user["username"],
                current_user["type"],
                "add_or_update_inventory",
            )

        elif choice == "2":
            item_name = input("Enter item name: ")
            print(f"Stock for {item_name}: {check_stock(item_name)}")
            write_user_usage(
                current_user["username"], current_user["type"], "check_stock"
            )

        elif choice == "3":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity adjustment (positive or negative): "))
            adjust_stock(item_name, quantity)
            write_user_usage(
                current_user["username"], current_user["type"], "adjust_stock"
            )

        elif choice == "4":
            order_id = input("Enter order ID: ")
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = int(input("Enter price: "))
            create_purchase_order(order_id, item_name, quantity, price)
            write_user_usage(
                current_user["username"], current_user["type"], "create_purchase_order"
            )

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
            write_user_usage(
                current_user["username"], current_user["type"], "modify_purchase_order"
            )

        elif choice == "6":
            order_id = input("Enter order ID: ")
            cancel_purchase_order(order_id)
            write_user_usage(
                current_user["username"], current_user["type"], "cancel_purchase_order"
            )

        elif choice == "7":
            order_id = input("Enter order ID: ")
            print(f"Status for order ID {order_id}: {get_order_status(order_id)}")
            write_user_usage(
                current_user["username"], current_user["type"], "get_order_status"
            )

        elif choice == "8":
            generate_report()
            write_user_usage(
                current_user["username"], current_user["type"], "inventory_report"
            )

        elif choice == "9":
            break
        else:
            print("Invalid choice, please try again.")
