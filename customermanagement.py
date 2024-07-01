# login function
def login(user_data_list):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for user in user_data_list:
        if user["username"] == username and user["password"] == password:
            if user["status"] == "approved":
                print("===================================")
                print("Login successful")
                print("===================================\n\n\n")
                approve_user(user_data_list=user_data_list)
            elif user["status"] == "pending":
                print("===================================")
                print("Your account is still not approved yet")
                print("===================================")
        else:
            print("===================================")
            print(
                "No account with such username and password found\nPlease register first"
            )
            print("===================================")
        break


# customer main menu
def approve_user(user_data_list):
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
    print("===================================")
    print("           Order Product           ")
    print("===================================")
    # get product from text file
    # TODO: change file name
    with open("product.txt", "r") as file:
        product = file.read()
        item_counter = 1
        for item in product:
            print(f"{item_counter}.{item['product_name']} - {item['price']}")
            item_counter += 1


def service_repair():
    pass


def modify_request():
    pass


def order_status():
    pass


def reports():
    pass
