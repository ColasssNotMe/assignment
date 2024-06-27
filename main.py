import json

# define variables
user_data_list = []

# retrive data from text file
with open("users.txt", "r+") as f:
    content = f.read()
    # check whether there's content in the file
    # if there's content:
    if content:
        user_data_list = json.loads(content)
        # clear the file after load the data
        with open("users.txt", "w") as f:
            pass
        f.close()
    # if there's no content:
    else:
        user_data_list = []
        f.close()

# First screen
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
    username = input("Enter your username: ")
    password = input("Enter your password: ")
elif choice == 2:
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
        try:
            id_number = int(id_number)
            break
        except ValueError:
            print("ID number must only contain number!")
            id_number = input("Enter your ID number: ")
    # append the data to user_data_list
    user_data_list.append(
        {
            "id": id_number,
            "username": new_username,
            "password": new_password,
            "status": "pending",
        }
    )
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
        f.close()
    print("===================================")
    print("You have successfully registered\nPlease wait for admin to approve")
    print("===================================")


elif choice == 3:
    exit()

# check if id is digit or not using try-catch statement
