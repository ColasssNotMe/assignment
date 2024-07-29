# TODO: DO NOT COMMIT FILE YET, DO PSEUDOCODE
# TODO: login when password false, it just break
# TODO: check for every possible selection error

# havent done: inventory, super user, admin


# TODO:check for register data if == None

# Super customer username: 101,password: 101
from crud import register_user, load_data
from customermanagement import customer_menu
from usermanagement import superuser_menu, admin_menu


def main():
    user_data_list = load_data()
    # read the file if it exists, otherwise create it
    with open("products.txt", "a") as f:
        f.close()
    with open("orders.txt", "a") as f:
        f.close()
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
    selection = int(input("Enter your choice: "))
    if selection == 1:
        register_user(user_data_list=user_data_list, user_type="customer")
    elif selection == 2:
        register_user(user_data_list=user_data_list, user_type="admin")


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
                    if user["type"] == "superuser":
                        superuser_menu(user_data_list=user_data_list)
                    elif user["type"] == "admin":
                        admin_menu()
                    # TODO: for customer, straight away pass user data to customer_menu to make process easier
                    elif user["type"] == "customer":
                        customer_menu(current_user=user)
                    # return user so that dont need to loop the list again and again
                    return user

                elif user["status"] == "pending":
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
