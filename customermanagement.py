from crud import update_user, delete_user, read_user


# login function


def superuser_menu(user_data_list):
    print("Currently logged in as Super User")
    print("---------------------------------")
    print("===================================")
    print("               Menu                ")
    print("===================================")
    print("1. Add Users")
    print("2. Verify New Customers")
    print("3. Modify Users")
    print("4. Disable User Access")
    print("5. Inquiry of User's system usage")
    print("6. Customer Order Status")
    print("7. Reports")
    # TODO: check for valid selection
    selection = int(input("Enter your selection: "))
    if selection == 3:
        print("===================================")
        print("            Modify Users           ")
        print("===================================")
        print("1. Update User")
        print("2. Delete User")
        selection = int(input("Enter your selection: "))
        if selection == 1:
            update_user()
        elif selection == 2:
            user_selection = input("Enter the username you want to delete: ")
            delete_user(user_data_list=user_data_list, username=user_selection)
            # save to file
            with open("users.txt", "w") as f:
                for record in user_data_list:
                    recordString = ",".join(record)
                    f.write(recordString)
                f.close()


def admin_menu(user_data_list):
    print("Currently logged in as Admin")
    print("---------------------------------")
    print("1. Verify New Customers")
    print("2. Customer Order Status")
    print("3. Reports")


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
