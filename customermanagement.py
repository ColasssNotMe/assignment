# login function
def login(user_data_list):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # check if the username and password is correct, and also if verified
    for user in user_data_list:
        for data in user:
            if data[1] == username and data[2] == password:
                if data[3] == "approved":
                    print("===================================")
                    print("Login successful")
                    print("===================================\n\n\n")
                    if data[4] == "superuser":
                        superuser_menu()
                    elif data[4] == "admin":
                        admin_menu()
                    elif data[4] == "user":
                        customer_menu()
                    break
                elif data[3] == "pending":
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


def superuser_menu():
    print("Currently logged in as Super User")
    print("---------------------------------\n\n")
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
    # paste your code here


def admin_menu():
    print("Currently logged in as Admin")
    print("---------------------------------\n\n")
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
