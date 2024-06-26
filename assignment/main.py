import json

# define variables
user_data_list = []


# First screen
print("===================================")
print("             Main Menu            ")
print("===================================")
print("1. Login")
print("2. Register")
print("3. Exit")
choice = input("Enter your choice: ")
while choice not in ["1", "2", "3"]:
    print("Invalid choice!")
    choice = input("Enter your choice: ")

# Login screen
if choice == "1":
    username = input("Enter your username: ")
    password = input("Enter your password: ")
elif choice == "2":
    new_username = input("Enter your username: ")
    new_password = input("Enter your password: ")
    reenter_password = input("Re-enter your password: ")
    # check if the password are same or not
    while new_password != reenter_password:
        print("Passwords do not match!")
        new_password = input("Enter your password: ")
        reenter_password = input("Re-enter your password: ")
    id_number = input("Enter your ID number: ")

    # check if id is digit or not using try-catch statement
    while True:
        try:
            id_number = int(id_number)
        except ValueError:
            print("ID number must only contain number!")
            id_number = input("Enter your ID number: ")

    # append the data to user_data_list
    user_data_list[id_number]

    # open users.txt if it exists, otherwise create it
    # ref : https://www.pythontutorial.net/python-basics/python-write-text-file/
    # using json: https://pynative.com/python-save-dictionary-to-file/
    with open("users.txt", "a") as f:
        # dump data into text file
        # ref: https://docs.python.org/3/library/json.html
        json.dump(
            user_data_list,
            f,
            indent=4,
        )
    print(
        "You have successfully registered\nPlease wait for admin to approve\n\n\n\n\n\n"
    )
    print("===================================")

    # testin opening file
    with open("users.txt", "r") as f:
        temp = json.loads(f)
        print(temp)
