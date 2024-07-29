from order_pages import page1, page2, page3
from inventory import load_data
import datetime as dt
from User_Management import Write_Inquiry_of_User_system_usage as log_user_activity
# Do finish basic function before do change username/password function
# FIXME: need to make customer able to see what are currently on service
# TODO:report
# TODO:modify request
# FIXME: when writing to the orders.txt, the index in falty, could be the file problem, so delete it and do it again, or maybe the checking index problem
# variable :
# c_order_list = all c list
# c_order_index_in_current_user_notpaid = the index of the item that is not paid, only count in 1 user, not include other user
# order_index_all = the index of the order, including other user
# current_user = all info of current user
# order_num_selection = the order number that user want to modify
# modify_selection = the selection of the user to add or remove item
# old_and_new_order_list_combined = the list of the old and new order combined
# item_name = the item name that user want to request service
# selection = the selection of the user
# checkout = the selection of the user to checkout
# payment = the selection of the user to pay now, pay later or cancel
# total = the total price of the order
# status_list = the list of the status of the order
# time_list = the list of the time of the order
# username = the username of the current user
# current_order_list = the list of the current order list
# current_page_product = the list of the current page product
# current_page = the current page
# len_shown_product = the length of the shown product
# all_product = the list of all product
# selection = the selection of the user
# order = the order of the user
# order_username = the username of the order
# time = the time of the order
# list_data = the list of the data
# data = the data of the file
# index = the index of the order
# status = the status of the order


def customer_menu(current_user):
    """_summary_

    Args:
        current_user (list): info about current login user
    """
    print("===================================")
    print("               Menu                ")
    print("===================================")
    print("1. Order product")
    print("2. Service / Repair")
    print("3. Modify request")
    print("4. Order status")
    print("5. Reports")
    selection = int(input("Enter your selection: "))
    while selection not in [1, 2, 3, 4, 5]:
        print("Invalid selection!")
        selection = int(input("Enter your selection: "))
    if selection == 1:
        order_product(current_page=1, current_user=current_user)
        log_user_activity(
            current_user["username"],
            "customer",
            "order_product",
        )
    elif selection == 2:
        service_repair(username=current_user["username"], current_user=current_user)
        log_user_activity(
            current_user["username"],
            "customer",
            "service_repair",
        )

    elif selection == 3:
        modify_request(username=current_user["username"], current_user=current_user)
        log_user_activity(
            current_user["username"],
            "customer",
            "modify_request",
        )

    elif selection == 4:
        order_status(username=current_user["username"], current_user=current_user)
        log_user_activity(
            current_user["username"],
            "customer",
            "order_status",
        )

    elif selection == 5:
        reports(username=current_user["username"])
        log_user_activity(
            current_user["username"],
            "customer",
            "reports",
        )


def order_product(current_page, current_user, current_order_list=None):
    """_summary_

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

    all_product = load_data()[0]

    while True:
        print("===================================")
        print("              Product              ")
        print("===================================")

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
            print("Adding product")
            print(current_page_product[int(selection) - 1])
            current_order_list.append(current_page_product[int(selection) - 1])

        elif selection in ["p1", "p2", "p3"]:
            order_product(current_page=int(selection[1]), current_user=current_user)
        elif selection == "b":
            print("Back to menu")
            customer_menu(current_user=current_user)
        elif selection == "c":
            print("Checking out...")
            print("Order list: ")

            # show the order list
            print("===================================")
            print("              Order List           ")
            print("===================================")
            counter = 1
            for product in current_order_list:
                print(f"{counter}.{product[0]} - {product[1]}")
                counter += 1
                simplified_current_order_list.append([product[0], product[1]])
            checkout = input("Confirm order? (y/n): ")
            while True:
                if checkout == "y":
                    # calculate total order price
                    total = 0
                    for item in simplified_current_order_list:
                        total += int(item[1])

                    print("===================================")
                    print("              Payment              ")
                    print("===================================")
                    print("Total price: ", total)
                    print("1. Pay Now")
                    print("2. Pay Later")
                    print("3. Cancel")
                    payment = input("Enter your selection: ")
                    time_now = str(dt.datetime.now())
                    if payment == "1":
                        print("------------Payment successful!-----------")
                        with open("orders.txt", "a") as f:
                            f.write(
                                str(
                                    {
                                        "username": username,
                                        "status": "paid",
                                        "time": time_now,
                                        "order": simplified_current_order_list,
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
                                        "username": username,
                                        "status": "notpaid",
                                        "time": time_now,
                                        "order": simplified_current_order_list,
                                    }
                                )
                            )
                            print(
                                "!!!Order successful!. Please pay as soon as possible in order to proceed!!!"
                            )
                            f.write("\n")
                        return customer_menu(current_user=current_user)
                    elif payment == "3":
                        print("----------Order cancelled----------")
                        current_order_list = []
                        pass
                elif checkout == "n":
                    print("----------Order cancelled----------")
                    return customer_menu(current_user=current_user)
                else:
                    print("------------Invalid selection!------------")
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
    print("-----------------------------------")
    print("Select order: ")
    if len(c_order_list) == 0:
        print("No order found!")
        return customer_menu(current_user=current_user)
    else:
        paid_order_list = []
        counter = 1
        for i in c_order_list:
            if i["status"] == "paid":
                print(f"{counter}.{i["status"]} - {i["time"]}")
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

    print("-----------------------------------")
    print("Order details: ")
    # show all order item
    counter = 1
    for i in range(len(paid_order_list[int(selection) - 1]["order"])):
        print(f"{counter}.{paid_order_list[int(selection) - 1]["order"][i][0]}")
        counter += 1
    request_service_selection = input("Enter the item you want to request service: ")
    while not (
        request_service_selection.isdigit()
        and 1 <= int(request_service_selection) <= len(paid_order_list)
    ):
        print("Invalid selection!")
        request_service_selection = input(
            "Enter the item you want to request service: "
        )
    # get the item name according to the request_service_selection
    item_name = paid_order_list[int(request_service_selection) - 1]["order"]
    time_now = str(dt.datetime.now())
    with open("service_repair.txt", "a") as f:
        f.write(str({"username": username, "time": time_now, "item": item_name}))
        f.write("\n")
        print("Service request sent!")
        return service_repair(username=username)


def modify_request(username, current_user):
    # get all item
    c_order_list = []
    with open("orders.txt", "r") as f:
        data = f.readlines()
        for order in data:
            order = eval(order)
            if order["username"] == username:
                c_order_list.append(order)

    print("-----------------------------------")
    print("Select the order you want to modify")
    print("-----------------------------------")
    c_order_list_notpaid = []
    counter = 1
    for i in c_order_list:
        if i["status"] == "notpaid":
            print(f"{counter}.{i["status"]} - {i["time"]}")
            c_order_list_notpaid.append(i)
            counter += 1

    if len(c_order_list_notpaid) == 0:
        print("No order found!")
        return customer_menu(current_user=username)
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
        return customer_menu(current_user=username)

    print("-----------------------------------")
    print("Order details: ")
    c_order_to_deal_with = c_order_list_notpaid[int(order_num_selection) - 1]
    counter = 1
    for item in c_order_to_deal_with["order"]:
        print(f"{counter}.{item[0]} - {item[1]}")
        old_and_new_order_list_combined = c_order_to_deal_with["order"]
    print("a. Add item")
    print("b. Remove item")
    modify_selection = input("Enter your selection: ")
    while modify_selection not in ["a", "b"]:
        print("Invalid selection!")
        modify_selection = input("Enter your selection: ")

    if modify_selection == "a":
        while True:
            return order_product(
                current_page=1,
                current_user=current_user,
                current_order_list=old_and_new_order_list_combined,
            )
    elif modify_selection == "b":
        print("!!!!!!!!!Warning!!!!!!!!!")
        # FIXME: havent change to dict
        for item in c_order_to_deal_with["order"]:
            print(f"{counter}.{item[0]} - {item[1]}")
            old_and_new_order_list_combined = c_order_to_deal_with["order"]
        remove_selection = input(
            "Enter the item you want to remove (Enter 0 to exit): "
        )
        while remove_selection != "0":
            while not (
                remove_selection.isdigit()
                and 1 <= int(remove_selection) <= len(c_order_to_deal_with["order"])
            ):
                print("Invalid selection!")
                remove_selection = input(
                    "Enter the item you want to remove (Enter 0 to exit): "
                )

            c_order_to_deal_with["order"].pop(int(remove_selection) - 1)
            # remove the old order from the list and also the text file

            print("Item removed!")
            for item in c_order_to_deal_with["order"]:
                print(f"{counter}.{item[0]} - {item[1]}")
                old_and_new_order_list_combined = c_order_to_deal_with["order"]
            if len(old_and_new_order_list_combined) == 0:
                print("Order empty!")
                return customer_menu(current_user=current_user)
            remove_selection = input(
                "Enter the item you want to remove (Enter 0 to exit): "
            )
        # write the new order to the file

        with open("orders.txt", "r+") as f:
            data = f.readlines()
            # remove the old order from the list and also the text file
            evaluated = eval(data)
            if (
                evaluated["username"] == c_order_to_deal_with["username"]
                and evaluated["time"] == c_order_to_deal_with["time"]
            ):
                with open("orders.txt", "a") as f:
                    f.write(
                        str(
                            {
                                "username": username,
                                "status": "notpaid",
                                "time": str(dt.datetime.now()),
                                "order": old_and_new_order_list_combined,
                            }
                        )
                    )
                    f.write("\n")
                    print("Order updated!")
                return customer_menu(current_user=current_user)

            else:
                print("Invalid selection!")
            pass
            # TODO: enable order to be cancel
    # TODO: when adding new item, it never append to the "old" list
    # TODO: overwrite the old item data after checkcout


def order_status(username, current_user):
    """check for the user all order and their status
    c_order_list = [item,price]

    """
    c_order_list = []
    status_list = []
    time_list = []
    with open("orders.txt", "r") as f:
        data = f.readlines()
        for order in data:
            list_data = order.split("/")
            order_username, status, time, order = list_data
            # convert the order string to list
            order = eval(order)
            if order_username == username:
                status_list.append(status)
                time_list.append(time)
                c_order_list.append(order)
    print("-----------------------------------")
    print("Select the order you want to check: ")
    if len(c_order_list) == 0:
        print("No order found!")
        return customer_menu(current_user=username)
    else:
        for i in range(len(c_order_list)):
            print(f"{i+1}.{status_list[i]} - {time_list[i]}")
        print("b. Back")
    selection = input("Enter the order number: ")
    while (
        not (selection.isdigit() and 1 <= int(selection) <= len(c_order_list))
        and selection != "b"
    ):
        print("Invalid selection!")
        selection = input("Enter the order number: ")

    if selection == "b":
        return customer_menu(current_user=username)
        print("-----------------------------------")
        print("Order details: ")
    """
    get the order = c_order_list[int(selection) - 1
    get the order item = c_order_list[int(selection) - 1][i][0]
    get the order price = c_order_list[int(selection) - 1][i][1]
    """
    total = 0
    # show all order item and price
    print("-----------------------------------")
    for i in range(len(c_order_list[int(selection) - 1])):
        print(
            f"{i+1}.{c_order_list[int(selection) - 1][i][0]} - {c_order_list[int(selection) - 1][i][1]}"
        )
        total += int(c_order_list[int(selection) - 1][i][1])
    print(f"Total price: {total}")
    if status_list[int(selection) - 1] == "notpaid":
        print("Payment not made yet!")
        print("1. Pay now")
        print("2. Modify order")
        print("3. Back to menu")
        selection = input("Enter your selection: ")
        if selection == "1":
            print("Payment successful!")
            status_list[int(selection) - 1] = "paid"
            return customer_menu(current_user=username)

        elif selection == "2":
            return modify_request(username=username, current_user=username)

        elif selection == "3":
            print("Back to menu")
            return customer_menu(current_user=username)
    else:
        print("b. Back")
        selection = input("Enter your selection: ")
        while selection != "b":
            print("Invalid selection!")
            selection = input("Enter your selection: ")
        else:
            return order_status(username=username)


def reports(username):
    all_order = []
    with open("order.txt", "r") as f:
        data = f.readlines()
        for order in data:
            order = eval(order)
            if order["username"] == username:
                all_order.append(order)
    print("-----------------------------------")
    print("--------------Reports--------------")
    print("-----------------------------------")
    print("1. Order history")
    print("2. Service history")
    print("3. Back")
    selection = input("Enter your selection: ")
    while selection not in ["1", "2", "3"]:
        print("Invalid selection!")
        selection = input("Enter your selection: ")
    if selection == "1":
        print("Order history: ")
        counter = 1
        for order in all_order:
            print(f"{counter}.{order}")
            counter += 1
        print("b. Back")
        selection = input("Enter your selection: ")
        while not (
            selection.isdigit()
            and 1 <= int(selection) <= len(all_order)
            or selection == "b"
        ):
            print("Invalid selection!")
            selection = input("Enter your selection: ")
        if selection == "b":
            return reports(username=username)
    elif selection == "2":
        print("Service history: ")
        with open("service_repair.txt", "r") as f:
            data = f.readlines()
            counter = 1
            record = eval(data)
            for record in data:
                pass
