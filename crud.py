def register_user(user_data_list, user_type: str):
    new_username = input("Enter your username: ")
    # check for usename null
    while new_username is None:
        print("Username cannot be empty!")
        new_username = input("Enter your username: ")
    new_password = input("Enter your password: ")
    reenter_password = input("Re-enter your password: ")
    # check if the password are same or not
    while new_password != reenter_password:
        print("Passwords does not match!")
        new_password = input("Enter your password: ")
        reenter_password = input("Re-enter your password: ")
    id_number = input("Enter your IC/passport number: ")
    # check for null and only number
    if id_number is None:
        print("ID number cannot be empty!")
        id_number = input("Enter your ID number: ")
    elif id_number.isdigit() is False:
        print("ID number must only contain number!")
        id_number = input("Enter your ID number: ")

    # append the data to user_data_list
    if user_type == "customer":
        user_data_list.append(
            [id_number, new_username, new_password, "pending", "customer", "\n"]
        )
        print("===================================")
        print("You have successfully registered\nPlease wait for admin to approve")
        print("===================================")
    elif user_type == "admin":
        user_data_list.append(
            [id_number, new_username, new_password, "pending", "admin", "\n"]
        )
        print("===================================")
        print("You have successfully registered\nPlease wait for Super User to approve")
        print("===================================")

    # clear the file
    with open("users.txt", "w") as f:
        pass
        f.close()
    # add data to the file
    with open("users.txt", "a") as f:
        # dump data into text file
        # ref: https://www.geeksforgeeks.org/what-does-s-mean-in-a-python-format-string/
        for record in user_data_list:
            recordString = ",".join(record)
            f.write(recordString)


# for delete,update, assign userdatalist to the function: user_data_list = delete_user(user_data_list, username)
def update_user(
    user_data_list, username, new_username, password, new_password, id: int, new_id: int
):
    for record in user_data_list:
        if record[1] == username:
            if new_username:
                record[1] = new_username
            if new_password:
                record[2] = new_password
            if new_id:
                record[0] = new_id


def delete_user(user_data_list, username):
    for record in user_data_list:
        if record[1] == username:
            user_data_list.remove(record)
    return user_data_list


def read_user():
    pass
