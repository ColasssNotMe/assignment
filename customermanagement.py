from order_pages import page1, page2, page3
from inventory import load_data
import datetime as dt
# Do finish basic function before do change username/password function
# FIXME: need to make customer able to see what are currently on service
# TODO:report
# TODO:modify request
# FIXME: when writing to the orders.txt, the index in falty, could be the file problem, so delete it and do it again, or maybe the checking index problem
# variable :
# all_ordered_item_list = all current user item list
# order_index_in_current_user_notpaid = the index of the item that is not paid, only count in 1 user, not include other user
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
    elif selection == 2:
        service_repair(username=current_user[1])
    elif selection == 3:
        modify_request(username=current_user[1], current_user=current_user)
    elif selection == 4:
        order_status(username=current_user[1], current_user=current_user)
    elif selection == 5:
        reports(username=current_user[1])


def order_product(current_page, current_user):
    """_summary_

    Args:
        current_page (int): get the current page
        current_user (list): current user list

    Returns:
        function: customer_menu
    """
    current_order_list = []
    current_page_product = []
    username = current_user[1]
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
                    if payment == "1":
                        print("------------Payment successful!-----------")
                        with open("orders.txt", "a") as f:
                            f.write(
                                f"{username}/paid/{dt.datetime.now()}/{simplified_current_order_list}"
                            )
                            f.write("\n")
                            print("Order placed!")
                            simplified_current_order_list = []
                        return customer_menu(current_user=current_user)
                    elif payment == "2":
                        print("Payment later")
                        with open("orders.txt", "a") as f:
                            f.write(
                                f"{username}/notpaid/{dt.datetime.now()}/{simplified_current_order_list}"
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
                    return customer_menu(current_user=current_user)
        else:
            print("Invalid selection!")
    return customer_menu(current_user=current_user)


def service_repair(username):
    all_ordered_item_list = []
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
                all_ordered_item_list.append(order)
    print("-----------------------------------")
    print("Select order: ")
    if len(all_ordered_item_list) == 0:
        print("No order found!")
        return customer_menu(current_user=username)
    else:
        for i in range(len(all_ordered_item_list)):
            if status_list[i] == "paid":
                print(f"{i+1}.{status_list[i]} - {time_list[i]}")
        print("b. Back")
    selection = input("Enter the order number: ")
    while (
        not (selection.isdigit() and 1 <= int(selection) <= len(all_ordered_item_list))
        and selection != "b"
    ):
        print("Invalid selection!")
        selection = input("Enter the order number: ")

    if selection == "b":
        return customer_menu(current_user=username)
    print("-----------------------------------")
    print("Order details: ")
    """
    get one whole order = all_ordered_item_list[int(selection) - 1
    get the order item = all_ordered_item_list[int(selection) - 1][i][0]
    get the order item with price = all_ordered_item_list[int(selection) - 1][i]
    get the order price = all_ordered_item_list[int(selection) - 1][i][1]
    """
    # show all order item
    for i in range(len(all_ordered_item_list[int(selection) - 1])):
        print(f"{i+1}.{all_ordered_item_list[int(selection) - 1][i][0]}")
    request_service_selection = input("Enter the item you want to request service: ")
    while not (
        request_service_selection.isdigit()
        and 1
        <= int(request_service_selection)
        <= len(all_ordered_item_list[int(selection) - 1])
    ):
        print("Invalid selection!")
        request_service_selection = input(
            "Enter the item you want to request service: "
        )
    # get the item name according to the request_service_selection
    item_name = all_ordered_item_list[int(selection) - 1][
        int(request_service_selection) - 1
    ][0]
    with open("service_repair.txt", "a") as f:
        f.write(f"{username}/{item_name}/{dt.datetime.now()}/service")
        f.write("\n")
        print("Service request sent!")
        return service_repair(username=username)


def modify_request(username, current_user):
    # get all item
    all_ordered_item_list = []
    status_list = []
    time_list = []
    old_and_new_order_list_combined = []
    order_index_all = []
    with open("orders.txt", "r") as f:
        data = f.readlines()
        index = -1
        for order in data:
            list_data = order.split("/")
            order_username, status, time, order = list_data
            # convert the order string to list
            index += 1
            order = eval(order)
            if order_username == username:
                status_list.append(status)
                time_list.append(time)
                all_ordered_item_list.append(order)
                order_index_all.append(index)

    print("-----------------------------------")
    print("Select the order you want to modify")
    print("-----------------------------------")
    if len(all_ordered_item_list) == 0:
        print("No order found!")
        return customer_menu(current_user=username)
    else:
        order_index_in_current_user_notpaid = []
        counter = 1
        for i in range(len(all_ordered_item_list)):
            if status_list[i] == "notpaid":
                print(f"{counter}.{status_list[i]} - {time_list[i]}")
                counter += 1
                order_index_in_current_user_notpaid.append(i)
        print("b. Back")
    order_num_selection = input("Enter the order number: ")
    while (
        not (order_num_selection.isdigit() and 1 <= int(order_num_selection) <= counter)
        and order_num_selection != "b"
    ):
        print("Invalid selection!")
        order_num_selection = input("Enter the order number: ")

    if order_num_selection == "b":
        return customer_menu(current_user=username)
    print("-----------------------------------")
    print("Order details: ")

    for i in range(
        len(
            all_ordered_item_list[
                order_index_in_current_user_notpaid[int(order_num_selection) - 1]
            ]
        )
    ):
        print(
            f"{i+1}.{all_ordered_item_list[order_index_in_current_user_notpaid[int(order_num_selection) - 1]][i][0]}"
        )
        old_and_new_order_list_combined.append(
            all_ordered_item_list[
                order_index_in_current_user_notpaid[int(order_num_selection) - 1]
            ][i]
        )

    print("a. Add item")
    print("b. Remove item")
    modify_selection = input("Enter your selection: ")
    while modify_selection not in ["a", "b"]:
        print("Invalid selection!")
        modify_selection = input("Enter your selection: ")

    if modify_selection == "a":
        # review this part
        current_page = 1
        current_page_product = []
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
                    len_shown_product, current_page_product = page2(
                        inventory=all_product
                    )
                else:
                    len_shown_product, current_page_product = page1(
                        inventory=all_product
                    )
            elif current_page == 3:
                if len(all_product) > 5:
                    len_shown_product, current_page_product = page3(
                        inventory=all_product
                    )
                else:
                    len_shown_product, current_page_product = page2(
                        inventory=all_product
                    )

            selection = input("Enter the product name you want to order: ")

            # check for shown product len to prevent index error
            if selection.isdigit() and int(selection) <= len_shown_product:
                print("Adding product")
                old_and_new_order_list_combined.append(
                    current_page_product[int(selection) - 1]
                )
            elif selection in ["p1", "p2", "p3"]:
                order_product(current_page=int(selection[1]), current_user=current_user)
            elif selection == "b":
                print("Back to menu")
                customer_menu(current_user=current_user)
            elif selection == "c":
                print("Checking out...")
                print("Order list: ")
                counter = 1
                for i in old_and_new_order_list_combined:
                    print(f"{counter}. {i[0]} - {i[1]}")
                    counter += 1
                checkout = input("Confirm order? (y/n): ")
                while True:
                    if checkout == "y":
                        # remove the old order from the list and also the text file

                        # calculate total order price
                        total = 0
                        for item in old_and_new_order_list_combined:
                            total += int(item[1])

                        print("===================================")
                        print("              Payment              ")
                        print("===================================")
                        print("Total price: ", total)
                        print("1. Pay Now")
                        print("2. Pay Later")
                        print("3. Cancel")
                        print(order_index_all)
                        order_to_delete = order_index_all[
                            order_index_in_current_user_notpaid[
                                int(order_num_selection) - 1
                            ]
                        ]
                        print(order_to_delete)

                        payment = input("Enter your selection: ")
                        if payment == "1":
                            with open("orders.txt", "r+") as f:
                                data = f.readlines()
                                toWrite = []
                                for order in data:
                                    list_data = order.split("/")
                                    toWrite.append(list_data)
                                toWrite.pop(order_to_delete)
                                f.seek(0)
                                f.truncate()
                                for item in toWrite:
                                    f.write("/".join(item))
                            print("------------Payment successful!-----------")
                            with open("orders.txt", "a") as f:
                                f.write(
                                    f"{username}/paid/{dt.datetime.now()}/{old_and_new_order_list_combined}"
                                )
                                f.write("\n")
                                print("Order placed!")
                                old_and_new_order_list_combined = []
                            return customer_menu(current_user=current_user)
                        elif payment == "2":
                            with open("orders.txt", "r+") as f:
                                data = f.readlines()
                                toWrite = []
                                for order in data:
                                    list_data = order.split("/")
                                    toWrite.append(list_data)
                                toWrite.pop(order_to_delete)
                                f.seek(0)
                                f.truncate()
                                for item in toWrite:
                                    f.write("/".join(item))
                            print("Pay later")
                            with open("orders.txt", "r+") as f:
                                f.write(
                                    f"{username}/notpaid/{dt.datetime.now()}/{old_and_new_order_list_combined}"
                                )
                                print(
                                    "!!!Order successful!. Please pay as soon as possible in order to proceed!!!"
                                )
                                f.write("\n")
                            return customer_menu(current_user=current_user)
                        elif payment == "3":
                            print("----------Order cancelled----------")
                            old_and_new_order_list_combined = []
                            return customer_menu(current_user=current_user)
                    elif checkout == "n":
                        print("----------Order cancelled----------")
                        return customer_menu(current_user=current_user)
                    else:
                        print("------------Invalid selection!------------")
    elif modify_selection == "b":
        return modify_request(username=username, current_user=current_user)
    else:
        print("Invalid selection!")
    pass
    # TODO: enable order to be cancel
    # TODO: when adding new item, it never append to the "old" list
    # TODO: overwrite the old item data after checkcout


def order_status(username, current_user):
    """check for the user all order and their status
    all_ordered_item_list = [item,price]

    """
    all_ordered_item_list = []
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
                all_ordered_item_list.append(order)
    print("-----------------------------------")
    print("Select the order you want to check: ")
    if len(all_ordered_item_list) == 0:
        print("No order found!")
        return customer_menu(current_user=username)
    else:
        for i in range(len(all_ordered_item_list)):
            print(f"{i+1}.{status_list[i]} - {time_list[i]}")
        print("b. Back")
    selection = input("Enter the order number: ")
    while (
        not (selection.isdigit() and 1 <= int(selection) <= len(all_ordered_item_list))
        and selection != "b"
    ):
        print("Invalid selection!")
        selection = input("Enter the order number: ")

    if selection == "b":
        return customer_menu(current_user=username)
        print("-----------------------------------")
        print("Order details: ")
    """
    get the order = all_ordered_item_list[int(selection) - 1
    get the order item = all_ordered_item_list[int(selection) - 1][i][0]
    get the order price = all_ordered_item_list[int(selection) - 1][i][1]
    """
    total = 0
    # show all order item and price
    print("-----------------------------------")
    for i in range(len(all_ordered_item_list[int(selection) - 1])):
        print(
            f"{i+1}.{all_ordered_item_list[int(selection) - 1][i][0]} - {all_ordered_item_list[int(selection) - 1][i][1]}"
        )
        total += int(all_ordered_item_list[int(selection) - 1][i][1])
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


def reports():
    pass
