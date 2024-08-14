# TODO: check for every possible selection error
# TODO:check for register data if ==

# ref: usertype : superuser, admin, staff, customer


# Super customer username: 101,password: 101
from crud import register_user, load_data
from customermanagement import customer_menu
from inventory import menu as inventory_menu
from User_Management import user_mangement_menu_admin, user_mangement_menu_superuser


def main():
    # read the file if it exists, otherwise create it
    with open("users.txt", "a") as f:
        pass
    with open("products.txt", "a") as f:
        pass
    with open("orders.txt", "a") as f:
        pass
    user_data_list = load_data()
    first_screen(user_data_list=user_data_list)


def first_screen(user_data_list):
    # First screen
    print("===================================")
    print("          Welcome to KLCCC         ")
    print("===================================")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    while choice not in [1, 2, 3]:
        print("Invalid choice!")
        choice = int(input("Enter your choice: "))

    # Login screen
    if choice == 1:
        login(user_data_list=user_data_list)
    # Register screen
    elif choice == 2:
        register_user(user_data_list=user_data_list, user_type="customer")
    elif choice == 3:
        exit()


# register function
def register(user_data_list):
    print("===================================")
    print("           Register as             ")
    print("===================================")
    print("1. Customer")
    print("2. Admin")
    print("3. Inventory Staff")
    selection = int(input("Enter your choice: "))
    if selection == 1:
        register_user(user_data_list=user_data_list, user_type="customer")
    elif selection == 2:
        register_user(user_data_list=user_data_list, user_type="admin")
    elif selection == 3:
        register_user(user_data_list=user_data_list, user_type="staff")


def login(user_data_list):
    # check if the username and password is correct, and also if verified

    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == "":
            print("Username cannot be empty")
            continue
        elif password == "":
            print("Password cannot be empty")
            continue
        login_successful = False
        for user in user_data_list:
            if username == user["username"] and password == user["password"]:
                if user["status"] == "approved":
                    print("===================================")
                    print("Login successful")
                    print("===================================\n\n\n")
                    login_successful = True
                    # change to list from dictionary
                    listing = list(
                        [
                            user["id"],
                            user["username"],
                            user["password"],
                            user["status"],
                            user["type"],
                            user["name"],
                            user["phone"],
                            user["address"],
                        ]
                    )
                    if user["type"] == "superuser":
                        user_mangement_menu_superuser(current_user=listing)
                    elif user["type"] == "admin":
                        user_mangement_menu_admin(current_user=listing)
                    # passing current user data to the function
                    elif user["type"] == "customer":
                        customer_menu(current_user=user)
                    elif user["type"] == "staff":
                        inventory_menu(current_user=user)

                elif (
                    user["status"] == "pending"
                    or user["status"] == "rejected"
                    or user["status"] == "disabled"
                ):
                    print("===================================")
                    print("Your account is still not approved yet")
                    print("===================================")
                    first_screen(user_data_list=user_data_list)

        if not login_successful:
            print("===================================")
            print("No account with such username or password found")
            print("===================================")
        else:
            break


main()
