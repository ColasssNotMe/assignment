from crud import update_user, delete_user, read_user


def customer_menu():
    print("===================================")
    print("               Menu                ")
    print("===================================")
    print("1. Order product")
    print("2. Service / Repair")
    print("3. Modify request")
    print("4. Order status")
    print("5. Reports")
    selection = int(input("Enter your selection: "))
    while selection not in [1, 2, 3, 4]:
        print("Invalid selection!")
        selection = input("Enter your selection: ")
    if selection == 1:
        order_product()
    elif selection == 2:
        service_repair()
    elif selection == 3:
        modify_request()
    elif selection == 4:
        order_status()
    elif selection == 5:
        reports()


def order_product():
    current_order_list = []
    with open("orders.txt", "a") as f:
        pass
        f.close()
    print("===================================")
    print("              Product              ")
    print("===================================")
    current_page = 1
    # TODO: need to pei he other user
    with open("products.txt", "r") as f:
        product = f.readlines()
        if current_page == 1:
            # show only 5 product per page
            for i in range(0, 5):
                # split the data
                for detail in product[i].split(","):
                    # print only the product name
                    print(detail[0])
        selection = int(input("Enter the product name you want to order: "))
    if selection not in [1, 2, 3, 4, 5]:
        print("Invalid selection!")
        selection = input("Enter your selection: ")
    if selection == 1:
        current_order_list.append()

        # get product from text file
        pass

    # get product from text file
    # TODO: change file name


def service_repair():
    pass


def modify_request():
    pass


def order_status():
    pass


def reports():
    pass
