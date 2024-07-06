from crud import update_user, delete_user


def superuser_menu(user_data_list):
    print("Currently logged in as Super User")
    print("---------------------------------")
    print("===================================")
    print("               Menu                ")
    print("===================================")
    print("1. Add Users")
    print("2. Verify New Customers")
    print("3. Modify Users")
    print("4. Disable User Access")
    print("5. Inquiry of User's system usage")
    print("6. Customer Order Status")
    print("7. Reports")
    # TODO: check for valid selection
    selection = int(input("Enter your selection: "))
    if selection == 3:
        print("===================================")
        print("            Modify Users           ")
        print("===================================")
        print("1. Update User")
        print("2. Delete User")
        selection = int(input("Enter your selection: "))
        if selection == 1:
            update_user()
        elif selection == 2:
            user_selection = input("Enter the username you want to delete: ")
            delete_user(user_data_list=user_data_list, username=user_selection)
            # save to file
            with open("users.txt", "w") as f:
                for record in user_data_list:
                    recordString = ",".join(record)
                    f.write(recordString)
                f.close()


def admin_menu(user_data_list):
    print("Currently logged in as Admin")
    print("---------------------------------")
    print("1. Verify New Customers")
    print("2. Customer Order Status")
    print("3. Reports")
