from order_pages import page1, page2, page3
from inventory import load_data
import datetime as dt
# Do finish basic function before do change username/password function
# FIXME: need to make customer able to see what are currently on service
# TODO:report
# TODO:modify request


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
                        break
                    elif payment == "3":
                        print("----------Order cancelled----------")
                        current_order_list = []
                        pass
                elif checkout == "n":
                    print("----------Order cancelled----------")
                    break
                else:
                    print("------------Invalid selection!------------")
                    pass
        else:
            print("Invalid selection!")
    return customer_menu(current_user=current_user)


def service_repair(username):
    order_item_list = []
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
                order_item_list.append(order)
    print("-----------------------------------")
    print("Select order: ")
    if len(order_item_list) == 0:
        print("No order found!")
        return customer_menu(current_user=username)
    else:
        for i in range(len(order_item_list)):
            if status_list[i] == "paid":
                print(f"{i+1}.{status_list[i]} - {time_list[i]}")
        print("b. Back")
    selection = input("Enter the order number: ")
    while (
        not (selection.isdigit() and 1 <= int(selection) <= len(order_item_list))
        and selection != "b"
    ):
        print("Invalid selection!")
        selection = input("Enter the order number: ")

    if selection == "b":
        return customer_menu(current_user=username)
    print("-----------------------------------")
    print("Order details: ")
    """
    get the order = order_item_list[int(selection) - 1
    get the order item = order_item_list[int(selection) - 1][i][0]
    get the order price = order_item_list[int(selection) - 1][i][1]
    """
    # show all order item
    for i in range(len(order_item_list[int(selection) - 1])):
        print(f"{i+1}.{order_item_list[int(selection) - 1][i][0]}")
    request_service_selection = input("Enter the item you want to request service: ")
    while not (
        request_service_selection.isdigit()
        and 1
        <= int(request_service_selection)
        <= len(order_item_list[int(selection) - 1])
    ):
        print("Invalid selection!")
        request_service_selection = input(
            "Enter the item you want to request service: "
        )
    # get the item name according to the request_service_selection
    item_name = order_item_list[int(selection) - 1][int(request_service_selection) - 1][
        0
    ]
    with open("service_repair.txt", "a") as f:
        f.write(f"{username}/{item_name}/{dt.datetime.now()}/service")
        f.write("\n")
        print("Service request sent!")
        return service_repair(username=username)


def modify_request(username, current_user):
    # get all item
    order_item_list = []
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
                order_item_list.append(order)
                # testing
    print("Order item list:", order_item_list)
    print("Status list:", status_list)
    print("Time list:", time_list)
    print("-----------------------------------")
    print("Select the order you want to modify")
    print("-----------------------------------")
    if len(order_item_list) == 0:
        print("No order found!")
        return customer_menu(current_user=username)
    else:
        for i in range(len(order_item_list)):
            real_item_number_list = []
            # might use this to find the order
            if status_list[i] == "notpaid":
                counter = 1
                print(f"{counter}.{status_list[i]} - {time_list[i]}")
                counter += 1
                real_item_number_list.append(i)
        print("b. Back")
    selection = input("Enter the order number: ")
    while (
        not (selection.isdigit() and 1 <= int(selection) <= len(real_item_number_list))
        and selection != "b"
    ):
        print("Invalid selection!")
        selection = input("Enter the order number: ")

    if selection == "b":
        return customer_menu(current_user=username)
    print("-----------------------------------")
    print("Order details: ")
    for i in range(len(order_item_list[real_item_number_list[int(selection) - 1]])):
        print(
            f"{i+1}.{order_item_list[real_item_number_list[int(selection) - 1]][i][0]}"
        )

    print("1. Add item")
    print("2. Remove item")
    modify_selection = input("Enter your selection: ")
    if modify_selection == "1":
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
                order_item_list.append(current_page_product[int(selection) - 1])

            elif selection in ["p1", "p2", "p3"]:
                order_product(current_page=int(selection[1]), current_user=current_user)
            elif selection == "b":
                print("Back to menu")
                customer_menu(current_user=current_user)
            elif selection == "c":
                print("Checking out...")
                print("Order list: ")
                for i in order_item_list:
                    counter = 1
                    print(f"{counter}. {i}")
                # TODO: show the order list


def order_status(username, current_user):
    """check for the user all order and their status
    order_item_list = [item,price]

    """
    order_item_list = []
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
                order_item_list.append(order)
    print("-----------------------------------")
    print("Select the order you want to check: ")
    if len(order_item_list) == 0:
        print("No order found!")
        return customer_menu(current_user=username)
    else:
        for i in range(len(order_item_list)):
            print(f"{i+1}.{status_list[i]} - {time_list[i]}")
        print("b. Back")
    selection = input("Enter the order number: ")
    while (
        not (selection.isdigit() and 1 <= int(selection) <= len(order_item_list))
        and selection != "b"
    ):
        print("Invalid selection!")
        selection = input("Enter the order number: ")

    if selection == "b":
        return customer_menu(current_user=username)
        print("-----------------------------------")
        print("Order details: ")
    """
    get the order = order_item_list[int(selection) - 1
    get the order item = order_item_list[int(selection) - 1][i][0]
    get the order price = order_item_list[int(selection) - 1][i][1]
    """
    total = 0
    # show all order item and price
    print("-----------------------------------")
    for i in range(len(order_item_list[int(selection) - 1])):
        print(
            f"{i+1}.{order_item_list[int(selection) - 1][i][0]} - {order_item_list[int(selection) - 1][i][1]}"
        )
        total += int(order_item_list[int(selection) - 1][i][1])
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
