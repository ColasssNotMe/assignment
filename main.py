# TODO: DO NOT COMMIT FILE YET, DO PSEUDOCODE
# notepad data sequence:
# id
# username
# password
# status
# type


# Super customer username: 101,password: 101
from customermanagement import login


def main():
    # read the file if it exists, otherwise create it
    with open("users.txt", "a+") as f:
        f.seek(0)
        # add superuser to the file if it is empty
        if f.read(1):
            f.seek(0)
            user_data_list = eval(f.read())

        else:
            user_data_list = [[101, "101", "101", "approved", "superuser"]]
            f.seek(0)
            f.write("%s\n" % user_data_list)
        f.close()

    # First screen
    print("===================================")
    print("          Welcome to KLCCC         ")
    print("===================================")
    print("===================================")
    print("             Main Menu            ")
    print("===================================")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    while choice not in [1, 2, 3]:
        print("Invalid choice!")
        choice = input("Enter your choice: ")

    # Login screen
    if choice == 1:
        login(user_data_list=user_data_list)
    # Register screen
    elif choice == 2:
        register(user_data_list=user_data_list)
    elif choice == 3:
        exit()

    # debugging purpose
    # with open("users.txt", "r") as f:
    #     user_data_list = eval(f.read())
    #     for user in user_data_list:
    #         for data in user:
    #             if data == "superuser":
    #                 print(user)
    #     f.close()


def saving_register_data(user_data_list, user_type: str):
    new_username = input("Enter your username: ")
    new_password = input("Enter your password: ")
    reenter_password = input("Re-enter your password: ")
    # check if the password are same or not
    while new_password != reenter_password:
        print("Passwords does not match!")
        new_password = input("Enter your password: ")
        reenter_password = input("Re-enter your password: ")
    id_number = input("Enter your IC/passport number: ")
    while True:
        # check if id is digit or not using try-except statement
        try:
            id_number = int(id_number)
            break
        except ValueError:
            print("ID number must only contain number!")
            id_number = input("Enter your ID number: ")
    # append the data to user_data_list
    if user_type == "customer":
        user_data_list.append(
            [
                id_number,
                new_username,
                new_password,
                "pending",
                "customer",
            ]
        )
        print("===================================")
        print("You have successfully registered\nPlease wait for admin to approve")
        print("===================================")
    elif user_type == "admin":
        user_data_list.append(
            [
                id_number,
                new_username,
                new_password,
                "pending",
                "admin",
            ]
        )
        print("===================================")
        print("You have successfully registered\nPlease wait for Super User to approve")
        print("===================================")
    # open users.txt if it exists, otherwise create it
    # ref : https://www.pythontutorial.net/python-basics/python-write-text-file/

    # clear the file
    with open("users.txt", "w") as f:
        pass
        f.close()
    # add data to the file
    with open("users.txt", "a") as f:
        # dump data into text file
        # ref: https://www.geeksforgeeks.org/what-does-s-mean-in-a-python-format-string/
        f.write("%s\n" % user_data_list)
        f.close()


# register function
def register(user_data_list):
    print("===================================")
    print("           Register as             ")
    print("===================================")
    print("1. Customer")
    print("2. Admin")
    selection = int(input("Enter your choice: "))
    if selection == 1:
        saving_register_data(user_data_list=user_data_list, user_type="customer")
    elif selection == 2:
        saving_register_data(user_data_list=user_data_list, user_type="admin")


if __name__ == "__main__":
    main()
