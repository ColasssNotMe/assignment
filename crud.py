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
    phone = input("Enter your phone number: ")
    while True:
        if phone is None:
            print("Phone number cannot be empty!")
            phone = input("Enter your phone number: ")
        elif phone.isdigit() is False:
            print("Phone number must only contain number!")
            phone = input("Enter your phone number: ")
        elif len(phone) != 10:
            print("Phone number must be 10 digit!")
            phone = input("Enter your phone number: ")
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
                "phone": phone,
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
                "phone": phone,
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
                    "phone": "010",
                    "address": "address",
                    "status": "approved",
                    "type": "superuser",
                },
                {
                    "id": "1",
                    "username": "1",
                    "password": "1",
                    "name": "Staff",
                    "phone": "010",
                    "address": "address",
                    "status": "approved",
                    "type": "staff",
                },
            ]

    return user_data_list


def conv_to_list(data):
    data_list = []
    if len(list(data)) == 1:
        listing = list(
            data["id"],
            data["username"],
            data["password"],
            data["status"],
            data["type"],
            data["name"],
            data["phone"],
            data["address"],
        )
        data_list.append(listing)
    else:
        for user in data:
            listing = list(
                (
                    user["id"],
                    user["username"],
                    user["password"],
                    user["status"],
                    user["type"],
                    user["name"],
                    user["phone"],
                    user["address"],
                )
            )
            data_list.append(listing)
    return data_list


def conv_to_dict(data):
    data_dict = []
    if len(list(data)) == 1:
        dict = {
            "id": data[0],
            "username": data[1],
            "password": data[2],
            "status": data[3],
            "type": data[4],
            "name": data[5],
            "address": data[7],
            "phone": data[6],
        }
        data_dict.append(dict)
    else:
        for record in data:
            dict = {
                "id": record[0],
                "username": record[1],
                "password": record[2],
                "status": record[3],
                "type": record[4],
                "name": record[5],
                "address": record[7],
                "phone": record[6],
            }
            data_dict.append(dict)
    return data_dict


def write_data(data, open_mode):
    if len(data) == 1:
        with open("users.txt", open_mode) as f:
            f.write(str(data) + "\n")
    else:
        with open("users.txt", open_mode) as f:
            for record in data:
                f.write(str(record) + "\n")
    return data
