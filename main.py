# TODO: DO NOT COMMIT FILE YET, DO PSEUDOCODE
# TODO: login when password false, it just break
# TODO: check for every possible selection error

# havent done: inventory, super user, admin
# customer management part still left with things related to order


# notepad data sequence:
# id
# username
# password
# status


# TODO:check for register data if ==null

# Super customer username: 101,password: 101
from crud import register_user
from customermanagement import customer_menu
from usermanagement import superuser_menu, admin_menu


def main():
    user_data_list = []
    # read the file if it exists, otherwise create it
    with open("users.txt", "a+") as f:
        # add superuser to the file if it is empty
        f.seek(0)
        data = f.readlines()
        if len(data) > 0:
            for record in data:
                recordList = record.split(",")
                user_data_list.append(recordList)
        else:
            user_data_list = [
                ["101", "101", "101", "approved", "superuser", "\n"],
                ["1", "1", "1", "approved", "customer", "\n"],
            ]
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
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # check if the username and password is correct, and also if verified
    for user in user_data_list:
        if username == user[1] and password == user[2]:
            if user[3] == "approved":
                print("===================================")
                print("Login successful")
                print("===================================\n\n\n")
                if user[4] == "superuser":
                    superuser_menu(user_data_list=user_data_list)
                elif user[4] == "admin":
                    admin_menu()
                # TODO: for customer, straight away pass user data to customer_menu to make process easier
                elif user[4] == "customer":
                    customer_menu(current_user=user)
                # return user so that dont need to loop the list again and again
                return user
                break
            elif user[3] == "pending":
                print("===================================")
                print("Your account is still not approved yet")
                print("===================================")
                break
            elif user[1] not in user_data_list:
                print("===================================")
                print("No account with such username or password found")
                print("===================================")
                first_screen(user_data_list=user_data_list)


main()
