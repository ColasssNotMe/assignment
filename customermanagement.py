# from crud import update_user, delete_user, read_user
from order_pages import page1, page2, page3
import datetime as dt
# Do finish basic function before do change username/password function
# TODO: payment page missed


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
        service_repair()
    elif selection == 3:
        modify_request()
    elif selection == 4:
        order_status(username=current_user[1])
    elif selection == 5:
        reports()


def order_product(current_page, current_user):
    """_summary_

    Args:
        current_page (int): get the current page
        current_user (list): current user list

    Returns:
        function: customer_menu
    """
    current_order_list = []
    all_product = []
    current_page_product = []
    username = current_user[1]
    simplified_current_order_list = []
    # init orders.txt
    with open("orders.txt", "a") as f:
        pass
        f.close()
        # TODO: need to pei he other user
        # read the product from text file
        # TODO: temp data
    temp_product = [
        "item1,",
        "price1,",
        "\n",
        "item1,",
        "price1,",
        "\n",
        "item1,",
        "price1,",
        "\n",
        "item1,",
        "price1,",
        "\n",
        "item1,",
        "price1,",
        "\n",
        "item1,",
        "price1,",
        "\n",
        "item1,",
        "price1,",
        "\n",
        "item1,",
        "price1,",
        "\n",
        "item1,",
        "price1,",
        "\n",
        "item1,",
        "price1,",
        "\n",
        "item1,",
        "price1,",
        "\n",
        "item1,",
        "price1,",
        "\n",
        "item1,",
        "price1,",
        "\n",
        "item1,",
        "price1,",
        "\n",
        "item1,",
        "price1,",
        "\n",
        "item1,",
        "price1,",
        "\n",
        "item1,",
        "price1,",
        "\n",
        "item1,",
        "price1,",
        "\n",
    ]
    with open("products.txt", "a") as f:
        f.writelines(temp_product)
    with open("products.txt", "r") as f:
        data = f.readlines()
        for product in data:
            product_list = product.split(",")
            all_product.append(product_list)
        f.close()
    while True:
        print("===================================")
        print("              Product              ")
        print("===================================")

        # len_shown_product : to know how many product shown in the page
        # current_order_list : to store the product that user want to order
        if current_page == 1:
            len_shown_product, current_page_product = page1(all_product=all_product)
        elif current_page == 2:
            if len(all_product) > 5:
                len_shown_product, current_page_product = page2(all_product=all_product)
            else:
                len_shown_product, current_page_product = page1(all_product=all_product)
        elif current_page == 3:
            if len(all_product) > 5:
                len_shown_product, current_page_product = page3(all_product=all_product)
            else:
                len_shown_product, current_page_product = page2(all_product=all_product)

        selection = input("Enter the product name you want to order: ")

        # check for shown product len to prevent index error
        if selection.isdigit() and int(selection) <= len_shown_product:
            print("Adding product")
            current_order_list.append(current_page_product[int(selection) - 1])

        elif selection in ["p1", "p2", "p3"]:
            order_product(current_page=int(selection[1]), current_user=current_user)
        elif selection == "b":
            print("Back to menu")
            break
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
                                f"[{username}/notpaid/{simplified_current_order_list}]"
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


# TODO: change file name


def service_repair():
    pass


def modify_request():
    pass


# TODO: do this function


def order_status(username):
    """check for the user all order and their status
    order_item = [item,price]

    """
    order_item = []
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
                order_item.append(order)
    print("Select the order you want to check: ")
    if len(order_item) == 0:
        print("No order found!")
    else:
        for i in range(len(order_item)):
            print(f"{i+1}.{status_list[i]} - {time_list[i]}")
        selection = input("Enter the order number: ")
        while not selection.isdigit() or int(selection) > len(order_item) + 1:
            print("Invalid selection!")
            selection = input("Enter the order number: ")
        print("Order details: ")
    """
    get the order = order_item[int(selection) - 1
    get the order item = order_item[int(selection) - 1][i][0]
    get the order price = order_item[int(selection) - 1][i][1]
    """
    for i in range(len(order_item[int(selection) - 1])):
        print(
            f"{i+1}.{order_item[int(selection) - 1][i][0]} - {order_item[int(selection) - 1][i][1]}"
        )


def reports():
    pass
