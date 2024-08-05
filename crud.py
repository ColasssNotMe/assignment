def register_user(user_data_list, user_type: str):
    new_username = input("Enter your username: ")
    # check for usename null
    while new_username is None:
        print("Username cannot be empty!")
        new_username = input("Enter your username: ")
    with open("users.txt", "r") as f:
        data = f.readlines()
        for user in data:
            user = eval(user)
            while True:
                if user["username"] == new_username:
                    print("Username already exists!")
                    new_username = input("Enter your username: ")
                else:
                    break
    new_password = input("Enter your password: ")
    reenter_password = input("Re-enter your password: ")
    # check if the password are same or not
    while new_password != reenter_password:
        print("Passwords does not match!")
        new_password = input("Enter your password: ")
        reenter_password = input("Re-enter your password: ")
    id_number = input("Enter your IC/passport number: ")
    # check for null and only number
    while True:
        if id_number is None:
            print("ID number cannot be empty!")
            id_number = input("Enter your ID number: ")
        elif id_number.isdigit() is False:
            print("ID number must only contain number!")
            id_number = input("Enter your ID number: ")
        elif len(id_number) != 12:
            print("ID number must be 12 digit!")
            id_number = input("Enter your ID number: ")
        else:
            break
    name = input("Enter your name: ")
    while name is None:
        print("Please enter your name!")
        name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    while True:
        if phone_number is None:
            print("Phone number cannot be empty!")
            phone_number = input("Enter your phone number: ")
        elif phone_number.isdigit() is False:
            print("Phone number must only contain number!")
            phone_number = input("Enter your phone number: ")
        elif len(phone_number) != 10:
            print("Phone number must be 10 digit!")
            phone_number = input("Enter your phone number: ")
        else:
            break
    address = input("Enter your address: ")
    while address is None:
        print("Address cannot be empty!")
        address = input("Enter your address: ")

    # append the data to user_data_list
    if user_type == "customer":
        user_data_list.append(
            {
                "id": id_number,
                "username": new_username,
                "password": new_password,
                "name": name,
                "phone_number": phone_number,
                "address": address,
                "status": "pending",
                "type": "customer",
            }
        )
        print("===================================")
        print("You have successfully registered\nPlease wait for admin to approve")
        print("===================================")
    elif user_type == "admin":
        user_data_list.append(
            {
                "id": id_number,
                "username": new_username,
                "password": new_password,
                "name": name,
                "phone_number": phone_number,
                "address": address,
                "status": "pending",
                "type": "admin",
            }
        )
        print("===================================")
        print("You have successfully registered\nPlease wait for Super User to approve")
        print("===================================")

    # clear the file
    with open("users.txt", "w") as f:
        # dump data into text file
        for record in user_data_list:
            f.write(str(record) + "\n")


# for delete,update, assign userdatalist to the function: user_data_list = delete_user(user_data_list, username)
def update_user(
    user_data_list, username, new_username, password, new_password, id: int, new_id: int
):
    for record in user_data_list:
        if record["username"] == username:
            if new_username:
                record["username"] = new_username
            if new_password:
                record["password"] = new_password
            if new_id:
                record["id"] = new_id


def delete_user(user_data_list, username):
    for record in user_data_list:
        if record["username"] == username:
            user_data_list.remove(record)
    return user_data_list


def load_data():
    with open("users.txt", "r+") as f:
        data = f.readlines()
        if len(data) > 0:
            user_data_list = []
            for record in data:
                record = record.replace(",\n", "")
                evaluated_record = eval(record)
                user_data_list.append(evaluated_record)
        else:
            user_data_list = [
                {
                    "id": "101",
                    "username": "101",
                    "password": "101",
                    "name": "Super User",
                    "phone_number": "010",
                    "address": "address",
                    "status": "approved",
                    "type": "superuser",
                },
                {
                    "id": "1",
                    "username": "1",
                    "password": "1",
                    "status": "approved",
                    "type": "customer",
                },
            ]

    return user_data_list
