# EUGENE CHING YI WEI
# TP077328

import datetime as dt
from GAN_ZHI_MING_TP075848 import load_data, add_or_update_inventory
from GAN_YEW_JUN_TP077400 import write_user_usage as log_user_activity
# Do finish basic function before do change username/password function
# TODO: need to make customer able to see what are currently on service
# TODO: add order id


def register_user(user_data_list, user_type: str):
    new_username = input("Enter your username: ")
    # check for usename null
    while new_username == "":
        print("Username cannot be empty!")
        new_username = input("Enter your username: ")
    with open("users.txt", "r") as f:
        data = f.readlines()
        for user in data:
            user = eval(user)
            while True:
                if user["username"] == new_username:
                    print("Username already exists!")
                    new_username = input("Enter your username: ")
                else:
                    break
    new_password = input("Enter your password: ")
    reenter_password = input("Re-enter your password: ")
    # check if the password are same or not
    while new_password != reenter_password:
        print("Passwords does not match!")
        new_password = input("Enter your password: ")
        reenter_password = input("Re-enter your password: ")
    id_number = input("Enter your IC/passport number: ")
    # check for null and only number
    while True:
        if id_number == "":
            print("ID number cannot be empty!")
            id_number = input("Enter your ID number: ")
        elif id_number.isdigit() is False:
            print("ID number must only contain number!")
            id_number = input("Enter your ID number: ")
        elif len(id_number) != 12:
            print("ID number must be 12 digit!")
            id_number = input("Enter your ID number: ")
        else:
            break
    name = input("Enter your name: ")
    while name == "":
        print("Please enter your name!")
        name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    while True:
        if phone == "":
            print("Phone number cannot be empty!")
            phone = input("Enter your phone number: ")
        elif phone.isdigit() is False:
            print("Phone number must only contain number!")
            phone = input("Enter your phone number: ")
        elif len(phone) not in (10, 11):
            print("Phone number must be 10 or 11 digit!")
            phone = input("Enter your phone number: ")
        else:
            break
    address = input("Enter your address: ")
    while address == "":
        print("Address cannot be empty!")
        address = input("Enter your address: ")

    # append the data to user_data_list
    if user_type == "customer":
        user_data_list.append(
            {
                "id": id_number,
                "username": new_username,
                "password": new_password,
                "name": name,
                "phone": phone,
                "address": address,
                "status": "pending",
                "type": "customer",
            }
        )
        print("=" * 50)
        print(f"{"You have successfully registered":<50}")
        print(f"{"Please wait for admin to approve":<50}")
        print("=" * 50)

    elif user_type == "stuff":
        user_data_list.append(
            {
                "id": id_number,
                "username": new_username,
                "password": new_password,
                "name": name,
                "phone": phone,
                "address": address,
                "status": "pending",
                "type": "stuff",
            }
        )
        print("=" * 50)
        print(f"{"You have successfully registered":<50}")
        print(f"{"Please wait for admin to approve":<50}")
        print("=" * 50)

    elif user_type == "admin":
        user_data_list.append(
            {
                "id": id_number,
                "username": new_username,
                "password": new_password,
                "name": name,
                "phone": phone,
                "address": address,
                "status": "pending",
                "type": "admin",
            }
        )
        print("=" * 50)
        print(f"{"You have successfully registered":<50}")
        print(f"{"Please wait for Super User to approve":<50}")
        print("=" * 50)

    # clear the file
    with open("users.txt", "w") as f:
        # dump data into text file
        for record in user_data_list:
            f.write(str(record) + "\n")


# for delete,update, assign userdatalist to the function: user_data_list = delete_user(user_data_list, username)
def update_user(
    user_data_list, username, new_username, password, new_password, id: int, new_id: int
):
    for record in user_data_list:
        if record["username"] == username:
            if new_username:
                record["username"] = new_username
            if new_password:
                record["password"] = new_password
            if new_id:
                record["id"] = new_id


def delete_user(user_data_list, username):
    for record in user_data_list:
        if record["username"] == username:
            user_data_list.remove(record)
    return user_data_list


def load_user_data():
    with open("users.txt", "r+") as f:
        data = f.readlines()
        if len(data) > 0:
            user_data_list = []
            for record in data:
                record = record.replace(",\n", "")
                evaluated_record = eval(record)
                user_data_list.append(evaluated_record)
        else:
            user_data_list = [
                {
                    "id": "101",
                    "username": "101",
                    "password": "101",
                    "name": "Super User",
                    "phone": "010",
                    "address": "address",
                    "status": "approved",
                    "type": "superuser",
                }
            ]

    return user_data_list


def process_dictionary(inventory):
    """convert dictionary from inventory to list

    Args:
        inventory (dict): inventory dictionary

    Returns:
        list: list of inventory
    """
    inventory_list = []
    for key, value in inventory.items():
        inventory_list.append([key, value])
    return inventory_list


def page1(inventory):
    inventory_list = process_dictionary(inventory)
    counter = 1
    current_page_product = inventory_list[0:5]
    # show only 5 product per page
    # print only the product name
    # if the thing too repetitive, can use function (elif part)
    for product in inventory_list:
        print(f"{counter}. {product[0]}")
        counter += 1
    print("p2. Page 2")
    print("p3. Page 3")
    print("c. Complete order")
    print("b. Back to main menu")

    return len(current_page_product), current_page_product


def page2(inventory):
    inventory_list = process_dictionary(inventory)
    counter = 1
    current_page_product = inventory_list[5:10]
    for product in inventory_list[5:]:
        print(f"{counter}. {product[0]}")
        counter += 1

    print("p1. Page 1")
    print("p3. Page 3")
    print("c. Complete order")
    print("b. Back to main menu")
    return len(current_page_product), current_page_product


def page3(inventory):
    inventory_list = process_dictionary(inventory)
    counter = 1
    current_page_product = inventory_list[10:15]
    for product in inventory_list[10:]:
        print(f"{counter}. {product[0]}")
        counter += 1
    print("p1. Page 1")
    print("p2. Page 2")
    print("c. Complete order")
    print("b. Back to main menu")
    return len(current_page_product), current_page_product


def customer_menu(current_user):
    """
    customer main menu
    Args:
        current_user (list): info about current login user
    """
    print("=" * 50)
    print(f"{'Menu':^50}")
    print("=" * 50)
    print("1. Order product")
    print("2. Service / Repair")
    print("3. Modify request")
    print("4. Order status")
    print("5. Reports")
    print("6. Exit")
    selection = input("Enter your selection: ")
    while selection not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid selection!")
        selection = input("Enter your selection: ")
    if selection == "1":
        order_products(current_page=1, current_user=current_user)
        log_user_activity(
            current_user["username"],
            "customer",
            "order_products",
        )
    elif selection == "2":
        service_repair(username=current_user["username"], current_user=current_user)
        log_user_activity(
            current_user["username"],
            "customer",
            "service_repair",
        )

    elif selection == "3":
        modify_request(username=current_user["username"], current_user=current_user)
        log_user_activity(
            current_user["username"],
            "customer",
            "modify_request",
        )

    elif selection == "4":
        order_status(username=current_user["username"], current_user=current_user)
        log_user_activity(
            current_user["username"],
            "customer",
            "order_status",
        )

    elif selection == "5":
        reports(username=current_user["username"], current_user=current_user)
        log_user_activity(
            current_user["username"],
            "customer",
            "customer_reports",
        )
    elif selection == "6":
        exit()


def order_products(
    current_page,
    current_user,
    current_order_list=None,
    remove_order=None,
    order_id=None,
):
    """
    order product function
    Args:
        current_page (int): get the current page
        current_user (list): current user list
    Returns:
        function: customer_menu
    """
    if current_order_list is None:
        current_order_list = []
    else:
        current_order_list = current_order_list
    current_page_product = []
    username = current_user["username"]
    simplified_current_order_list = []

    # init orders.txt
    with open("orders.txt", "a") as f:
        pass

    # remove item that have 0 stock
    high_stock_item_list = {}
    key_to_removed = []
    check_stock = load_data()[0]
    for key, value in check_stock.items():
        if value != 0:
            high_stock_item_list.update({key: value})
    all_product = load_data()[2]
    for key, item in all_product.items():
        if key not in high_stock_item_list:
            key_to_removed.append(key)
    for key in key_to_removed:
        all_product.pop(key)
    if len(all_product) == 0:
        print("No product available!")
        return customer_menu(current_user=current_user)

    while True:
        print("=" * 50)
        print(f"{'Product':^50}")
        print("=" * 50)
        # len_shown_product : to know how many product shown in the page
        # current_order_list : to store the product that user want to order
        if current_page == 1:
            len_shown_product, current_page_product = page1(inventory=all_product)
        elif current_page == 2:
            if len(all_product) > 5:
                len_shown_product, current_page_product = page2(inventory=all_product)
            else:
                len_shown_product, current_page_product = page1(inventory=all_product)
        elif current_page == 3:
            if len(all_product) > 5:
                len_shown_product, current_page_product = page3(inventory=all_product)
            else:
                len_shown_product, current_page_product = page2(inventory=all_product)

        selection = input("Enter the product name you want to order: ")
        # check for shown product len to prevent index error
        if selection.isdigit() and int(selection) <= len_shown_product:
            # reduce the stock of the product
            for itemname, number in high_stock_item_list.items():
                if current_page_product[int(selection) - 1][0] == itemname:
                    if number == 0:
                        print("Product out of stock!")
                        return order_products(
                            current_page=current_page, current_user=current_user
                        )
                    else:
                        print("Adding product")
                        high_stock_item_list[itemname] -= 1
                        current_order_list.append(
                            current_page_product[int(selection) - 1]
                        )

        elif selection in ["p1", "p2", "p3"]:
            order_products(current_page=int(selection[1]), current_user=current_user)
        elif selection == "b":
            print("Back to menu")
            # revert back the total number of product ordered
            for item in current_order_list:
                if item[0] in high_stock_item_list:
                    high_stock_item_list[item[0]] += 1
            customer_menu(current_user=current_user)
        elif selection == "c":
            print("Checking out...")
            print("Order list: ")

            # show the order list
            print("=" * 50)
            print(f"{'':<5}{'Order List':^40}")
            print("=" * 50)
            counter = 1
            print(f"{'':<5}{'Item':<30}{'Price':<15}")
            print("-" * 50)
            for product in current_order_list:
                print(f"{counter:<5}{product[0]:<30} {product[1]:<15}")
                counter += 1
                simplified_current_order_list.append([product[0], product[1]])
            checkout = input("Confirm order? (y/n): ")
            while True:
                if checkout == "y":
                    # calculate total order price
                    total = 0
                    # simplified_current_order_list = [item, price]
                    for item in simplified_current_order_list:
                        total += int(item[1])

                    print("=" * 50)
                    print(f"{'Payment':^50}")
                    print("=" * 50)
                    print("Total price: ", total)
                    print("1. Pay Now")
                    print("2. Pay Later")
                    print("3. Cancel")
                    payment = input("Enter your selection: ")
                    time_now = str(dt.datetime.now().replace(microsecond=0))
                    # get the latest order id
                    latest_order_id = 0
                    with open("orders.txt", "r") as f:
                        data = f.readlines()
                        if len(data) == 0:
                            latest_order_id = 1
                        for item in data:
                            item = eval(item)
                            if item["order_id"] >= latest_order_id:
                                latest_order_id = item["order_id"] + 1
                    if payment == "1":
                        print("-" * 50)
                        print(f"{'Payment Successfull':^50}")
                        print("-" * 50)
                        # update the number of product in the inventory
                        for item in simplified_current_order_list:
                            if item[0] in high_stock_item_list:
                                price = all_product.get(item[0])
                                quantity = high_stock_item_list.get(item[0])
                                add_or_update_inventory(
                                    item_name=item[0], quantity=quantity, price=price
                                )
                        # remove the order from the list if the user add product from modify func
                        if remove_order:
                            with open("orders.txt", "r") as f:
                                lines = f.readlines()
                            with open("orders.txt", "w") as f:
                                for record in lines:
                                    record = eval(record)
                                    if order_id == record["order_id"]:
                                        continue
                                    f.write(str(record) + "\n")
                                f.flush()

                        # write the order to the file
                        with open("orders.txt", "a") as f:
                            f.write(
                                str(
                                    {
                                        "order_id": latest_order_id,
                                        "username": username,
                                        "status": "paid",
                                        "time": time_now,
                                        "order": simplified_current_order_list,
                                        "send_status": "pending",
                                    }
                                )
                            )
                            f.write("\n")
                            print("Order placed!")
                            simplified_current_order_list = []
                        return customer_menu(current_user=current_user)
                    elif payment == "2":
                        print("Payment later")
                        with open("orders.txt", "a") as f:
                            f.write(
                                str(
                                    {
                                        "order_id": latest_order_id,
                                        "username": username,
                                        "status": "notpaid",
                                        "time": time_now,
                                        "order": simplified_current_order_list,
                                        "send_status": "pending",
                                    }
                                )
                            )
                            print(
                                f"{'!!!Order successful!. Please pay as soon as possible in order to proceed!!!':<50}"
                            )
                            f.write("\n")
                        # remove the order from the list if the user add product from modify func

                        if remove_order:
                            print("Removing order")
                            with open("orders.txt", "r") as f:
                                lines = f.readlines()
                            with open("orders.txt", "w") as f:
                                for record in lines:
                                    record = eval(record)
                                    if order_id == record["order_id"]:
                                        continue
                                    f.write(str(record) + "\n")
                                f.flush()

                        return customer_menu(current_user=current_user)
                    elif payment == "3":
                        print("-" * 50)
                        print(f"{'Order Cancelled':^50}")
                        print("-" * 50)
                        current_order_list = []
                        for item in current_order_list:
                            if item[0] in high_stock_item_list:
                                high_stock_item_list[item[0]] += 1
                        return customer_menu(current_user=current_user)
                elif checkout == "n":
                    print("-" * 50)
                    print(f"{'Order Cancelled':^50}")
                    print("-" * 50)
                    for item in current_order_list:
                        if item[0] in high_stock_item_list:
                            high_stock_item_list[item[0]] += 1
                    return customer_menu(current_user=current_user)
                else:
                    print(f"{'-':<10}{'Invalid selection':<30}{'-':<10}")
                    checkout = input("Confirm order? (y/n): ")
        else:
            print("Invalid selection!")
    return customer_menu(current_user=current_user)


def service_repair(current_user, username):
    c_order_list = []
    with open("orders.txt", "r") as f:
        data = f.readlines()
        for order in data:
            order = eval(order)
            if order["username"] == username:
                c_order_list.append(order)
    print("-" * 50)
    print("Select order: ")
    if len(c_order_list) == 0:
        print("No order found!")
        return customer_menu(current_user=current_user)
    else:
        paid_order_list = []
        counter = 1
        for i in c_order_list:
            if i["status"] == "paid":
                print(f"{counter}.{i['status']} - {i['time']}")
                paid_order_list.append(i)
                counter += 1
        print("b. Back")
    selection = input("Enter the order number: ")
    while (
        not (selection.isdigit() and 1 <= int(selection) <= len(paid_order_list))
        and selection != "b"
    ):
        print("Invalid selection!")
        selection = input("Enter the order number: ")

    if selection == "b":
        return customer_menu(current_user=current_user)

    request_service_selection = ""
    item_list = []
    while request_service_selection != "c":
        print("-" * 50)
        print("Order details: ")
        # show all order item
        counter = 1
        current_paid_order = paid_order_list[int(selection) - 1]
        for i in range(len(current_paid_order["order"])):
            print(f"{counter}.{current_paid_order['order'][i][0]}")
            counter += 1
        print("c. Continue")
        print("b. Back")
        request_service_selection = input(
            "Enter the item you want to request service: "
        )
        while not (
            (
                request_service_selection.isdigit()
                and 1
                <= int(request_service_selection)
                <= len(current_paid_order["order"])
            )
            or request_service_selection == "c"
            or request_service_selection == "b"
        ):
            print("Invalid selection!")
            request_service_selection = input(
                "Enter the item you want to request service: "
            )
        # get the item name according to the request_service_selection
        if request_service_selection == "c":
            break
        elif request_service_selection == "b":
            return customer_menu(current_user=current_user)
        else:
            item_name = current_paid_order["order"][int(request_service_selection) - 1][
                0
            ]
            if item_name not in item_list:
                item_list.append(item_name)
                time_now = str(dt.datetime.now().replace(microsecond=0))
            else:
                print("Item already in the list!")
    with open("service_repair.txt", "a") as f:
        f.write(str({"username": username, "time": time_now, "item": item_list}))
        f.write("\n")
        print("Service request sent!")
        return service_repair(username=username, current_user=current_user)
    f.flush()


def modify_request(username, current_user):
    # get all item
    c_order_list = []
    with open("orders.txt", "r") as f:
        data = f.readlines()
        for order in data:
            order = eval(order)
            if order["username"] == username:
                c_order_list.append(order)

    print("-" * 50)
    print(f"{'Select the order you want to modify':^50}")
    print("-" * 50)
    c_order_list_notpaid = []
    counter = 1
    for i in c_order_list:
        if i["status"] == "notpaid":
            print(f"{counter}.{i['status']} - {i['time']}")
            c_order_list_notpaid.append(i)
            counter += 1

    if len(c_order_list_notpaid) == 0:
        print("No order found!")
        return customer_menu(current_user=current_user)
    else:
        print("b. Back")
    order_num_selection = input("Enter the order number: ")
    while (
        not (
            order_num_selection.isdigit()
            and 1 <= int(order_num_selection) <= len(c_order_list_notpaid)
        )
        and order_num_selection != "b"
    ):
        print("Invalid selection!")
        order_num_selection = input("Enter the order number: ")

    if order_num_selection == "b":
        return customer_menu(current_user=current_user)

    print("-" * 50)
    print("Order details: ")
    c_order_to_deal_with = c_order_list_notpaid[int(order_num_selection) - 1]
    counter = 1
    for item in c_order_to_deal_with["order"]:
        print(f"{counter}.{item[0]} - {item[1]}")
        counter += 1
        old_and_new_order_list_combined = c_order_to_deal_with["order"]
    print("a. Add item")
    print("b. Remove item")
    print("c. Remove order")
    print("d. Back")
    modify_selection = input("Enter your selection: ")
    while modify_selection not in ["a", "b", "c", "d"]:
        print("Invalid selection!")
        modify_selection = input("Enter your selection: ")

    if modify_selection == "a":
        order_id = c_order_to_deal_with.get("order_id", "default_id")
        return order_products(
            current_page=1,
            current_user=current_user,
            current_order_list=old_and_new_order_list_combined,
            remove_order=True,
            order_id=order_id,
        )
    elif modify_selection == "b":
        print("!!!!!!!!!Warning!!!!!!!!!")
        counter = 1
        for item in c_order_to_deal_with["order"]:
            print(f"{counter}.{item[0]} - {item[1]}")
            counter += 1
            old_and_new_order_list_combined = c_order_to_deal_with["order"]
        remove_selection = input(
            'Enter the item you want to remove (Enter "b" to exit): '
        )
        while remove_selection != "b":
            while not (
                remove_selection.isdigit()
                and 1 <= int(remove_selection) <= len(c_order_to_deal_with["order"])
            ):
                print("Invalid selection!")
                remove_selection = input(
                    'Enter the item you want to remove (Enter "b" to exit): '
                )
            c_order_to_deal_with["order"].pop(int(remove_selection) - 1)
            # remove the old order from the list and also the text file
            print("Item removed!")
            counter = 1
            for item in c_order_to_deal_with["order"]:
                print(f"{counter}.{item[0]} - {item[1]}")
                counter += 1
                old_and_new_order_list_combined = c_order_to_deal_with["order"]
            if len(old_and_new_order_list_combined) == 0:
                print("Order empty!")
                return customer_menu(current_user=current_user)
            remove_selection = input(
                'Enter the item you want to remove (Enter "b" to exit): '
            )

        if remove_selection == "b":
            # write the new order to the file
            with open("orders.txt", "r+") as f:
                updated_data = []
                data = f.readlines()
                # remove the old order from the list and also the text file
                for record in data:
                    evaluated = eval(record)
                    if (
                        evaluated["username"] == c_order_to_deal_with["username"]
                        and evaluated["time"] == c_order_to_deal_with["time"]
                    ):
                        updated_data.append(
                            {
                                "order_id": evaluated["order_id"],
                                "username": username,
                                "status": "notpaid",
                                "time": str(dt.datetime.now().replace(microsecond=0)),
                                "order": old_and_new_order_list_combined,
                            }
                        )
                    else:
                        updated_data.append(evaluated)
                        print("Item removed!")
            with open("orders.txt", "w") as f:
                for record in updated_data:
                    f.write(str(record))
                    f.write("\n")
            return customer_menu(current_user=current_user)

    elif modify_selection == "c":
        with open("orders.txt", "r") as f:
            lines = f.readlines()
        with open("orders.txt", "w") as f:
            for record in lines:
                record = eval(record)
                if (
                    record["username"] == c_order_to_deal_with["username"]
                    and record["time"] == c_order_to_deal_with["time"]
                ):
                    print("Order removed!")
                    print("Money will be refunded to your account in 3-5 working days")
                    continue
                f.write(str(record) + "\n")
            f.flush()
            return modify_request(username=username, current_user=current_user)
    elif modify_selection == "d":
        return customer_menu(current_user=current_user)
    else:
        print("Invalid selection!")


def order_status(username, current_user):
    """check for the user all order and their status
    c_order_list = [item,price]

    """
    c_order_list = []
    with open("orders.txt", "r") as f:
        data = f.readlines()
        for order in data:
            order = eval(order)
            if order["username"] == username:
                c_order_list.append(order)
    print("-" * 50)
    print("Select the order you want to check: ")
    if len(c_order_list) == 0:
        print("No order found!")
        return customer_menu(current_user=current_user)
    else:
        for i in range(len(c_order_list)):
            send_status = c_order_list[i].get("send_status", "Status not available")
            print(f"{i+1}. {send_status} - {c_order_list[i]['time']}")
        print("b. Back")
    selection = input("Enter the order number: ")
    while (
        not (selection.isdigit() and 1 <= int(selection) <= len(c_order_list))
        and selection != "b"
    ):
        print("Invalid selection!")
        selection = input("Enter the order number: ")

    if selection == "b":
        return customer_menu(current_user=current_user)
        print("-" * 50)
        print("Order details: ")
    else:
        selected_order = c_order_list[int(selection) - 1]
    total = 0
    # show all order item and price
    print("-" * 50)
    for i in range(len(selected_order["order"])):
        print(
            f"{i+1}.{selected_order['order'][i][0]} - {selected_order['order'][i][1]}"
        )
        total += int(selected_order["order"][i][1])
    print(f"Total price: {total}")
    if selected_order["status"] == "notpaid":
        print("Payment not made yet!")
        print("1. Pay now")
        print("2. Modify order")
        print("3. Back to menu")
        selection = input("Enter your selection: ")
        if selection == "1":
            print("Payment successful!")
            # update the status in the file
            updated_data = []
            with open("orders.txt", "r+") as f:
                data = f.readlines()
                for record in data:
                    record = eval(record)
                    if (
                        record["username"] == username
                        and record["time"] == selected_order["time"]
                    ):
                        record["status"] = "paid"
                    updated_data.append(record)
            print(updated_data)
            with open("orders.txt", "w") as f:
                for record in updated_data:
                    f.write(str(record))
                    f.write("\n")
            return customer_menu(current_user=current_user)

        elif selection == "2":
            return modify_request(username=username, current_user=current_user)

        elif selection == "3":
            print("Back to menu")
            return customer_menu(current_user=current_user)
    else:
        print("b. Back")
        selection = input("Enter your selection: ")
        while selection != "b":
            print("Invalid selection!")
            selection = input("Enter your selection: ")
        else:
            return order_status(username=username, current_user=current_user)


def reports(username, current_user):
    with open("orders.txt", "r") as f:
        all_order = []
        data = f.readlines()
        for order in data:
            order = eval(order)
            if order["username"] == username:
                all_order.append(order)
    print("-" * 50)
    print(f"{"Reports":<50}")
    print("-" * 50)
    print("1. Order history")
    print("2. Service history")
    print("3. Back")
    selection = input("Enter your selection: ")
    while selection not in ["1", "2", "3"]:
        print("Invalid selection!")
        selection = input("Enter your selection: ")
    if selection == "1":
        print("-" * 50)
        print("Order history: ")
        counter = 1
        for order in all_order:
            print(f"{counter}.{order['time']}")
            counter += 1
        print("b. Back")
        selection = input("Enter your selection: ")
        while not (
            (selection.isdigit() and 1 <= int(selection) <= len(all_order))
            or selection == "b"
        ):
            print("Invalid selection!")
            selection = input("Enter your selection: ")
        if selection == "b":
            return reports(username=username, current_user=current_user)
        else:
            print("-" * 50)
            print("Order details: ")
            counter = 1
            total = 0
            for record in all_order[int(selection) - 1]["order"]:
                print(f"{counter}.{record[0]}")
                counter += 1
                total += int(record[1])
            print(f"Total price: {total}")
            print("b. Back")
            selection = input("Enter your selection: ")
            while selection != "b":
                print("Invalid selection!")
                selection = input("Enter your selection: ")
            else:
                return reports(username=username, current_user=current_user)
    elif selection == "2":
        all_order = []
        print("-" * 50)
        print("Service history: ")
        with open("service_repair.txt", "r") as f:
            data = f.readlines()
            counter = 1
            for record in data:
                record = eval(record)
                if record["username"] == username:
                    print(f"{counter}.{record['time']}")
                    all_order.append(record)
                    counter += 1
            print("b. Back")
            selection = input("Enter your selection: ")
            while not (1 <= int(selection) <= len(data) or selection == "b"):
                print("Invalid selection!")
                selection = input("Enter your selection: ")
            if selection == "b":
                return reports(username=username, current_user=current_user)
            else:
                print("-" * 50)
                print("Service details: ")
                counter = 1
                with open("service_repair.txt", "r") as f:
                    data = f.readlines()
                    for record in data:
                        record = eval(record)
                        if (
                            record["username"] == username
                            and record["time"] == all_order[int(selection) - 1]["time"]
                        ):
                            print(f"{counter}.{record['item'][counter-1]}")
                            counter += 1
                print("b. Back")
                selection = input("Enter your selection: ")
                while selection != "b":
                    print("Invalid selection!")
                    selection = input("Enter your selection: ")
                else:
                    return reports(username=username, current_user=current_user)
    elif selection == "3":
        return customer_menu(current_user=current_user)
