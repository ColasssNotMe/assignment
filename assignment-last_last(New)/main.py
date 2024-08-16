# TODO: check for every possible selection error
# TODO:check for register data if ==

# ref: usertype : superuser, admin, staff, customer


# Super customer username: 101,password: 101
from EUGENE_CHING_YI_WEI_TP077328 import (
    customer_menu,
    register_user,
    load_user_data,
)
from GAN_ZHI_MING_TP075848 import menu as inventory_menu
from GAN_YEW_JUN_TP077400 import (
    user_mangement_menu_admin,
    user_mangement_menu_superuser,
)


def main():
    # read the file if it exists, otherwise create it
    with open("users.txt", "a") as f:
        pass
    with open("products.txt", "a") as f:
        pass
    with open("orders.txt", "a") as f:
        pass
    with open("INVENTORY_DATA.txt", "a") as f:
        pass
    with open("user_usage.txt", "a") as f:  # noqa: F841
        pass
    user_data_list = load_user_data()
    first_screen(user_data_list=user_data_list)


def first_screen(user_data_list):
    # First screen
    print("=" * 50)
    print(f"{"Welcome to KLCCC":<50}")
    print("=" * 50)
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = input("Enter your choice: ")
    while choice not in ["1", "2", "3"]:
        print("Invalid choice!")
        choice = input("Enter your choice: ")

    # Login screen
    if choice == "1":
        login(user_data_list=user_data_list)
    # Register screen
    elif choice == "2":
        register(user_data_list=user_data_list)
    elif choice == "3":
        exit()


# register function
def register(user_data_list):
    print("=" * 50)
    print(f"{"Register as":<50}")
    print("=" * 50)
    print("1. Customer")
    print("2. Admin")
    print("3. Inventory Staff")
    selection = input("Enter your choice: ")
    while selection not in ["1", "2", "3"]:
        print("=" * 50)
        print(f"{"Register as":<50}")
        print("=" * 50)
        print("1. Customer")
        print("2. Admin")
        print("3. Inventory Staff")
        selection = input("Enter your choice: ")
    if selection == "1":
        register_user(user_data_list=user_data_list, user_type="customer")
    elif selection == "2":
        register_user(user_data_list=user_data_list, user_type="admin")
    elif selection == "3":
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
                    print("=" * 50)
                    print(f"{"Register as":<50}")
                    print("=" * 50)
                    print("\n\n\n")
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
                    print("=" * 50)
                    print(f"{"Your account is still not approved yet":<50}")
                    print("=" * 50)
                    first_screen(user_data_list=user_data_list)

        if not login_successful:
            print("=" * 50)
            print(f"{"No account with such username or password found":<50}")
            print("=" * 50)
        else:
            break


main()
