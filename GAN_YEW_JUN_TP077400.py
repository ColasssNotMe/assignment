#GAN YEW JUN  
#TP077400   

def load_data():
    with open("users.txt", "r+") as f:
        data = f.readlines()
        user_data_list = []
        for record in data:
            record = record.replace(",\n", "")
            evaluated_record = eval(record)
            user_data_list.append(evaluated_record)
    return user_data_list


def conv_to_list(data):
    data_list = []
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
    with open("users.txt", open_mode) as f:
        for item in data:
            f.write(str(item) + "\n")


def check_id(new_id_number,func_back_to,current_user):
    while True:
        if new_id_number =="":
            print("IC number cannot be empty!")
            new_id_number = input("Please enter IC number: ")
        elif new_id_number == "b":
            back_to_menu(func_back_to,current_user)
        elif new_id_number.isdigit() is False:
            print("IC number must only contain number!")
            new_id_number = input("Please re-enter IC number: ")
        elif len(new_id_number) != 12:
            print("IC number must be 12 digit!")
            new_id_number = input("Please re-enter IC number: ")
        else:
            break
    return new_id_number
    

def check_username(new_username,func_back_to,current_user):
    #get data from users.txt
    file_data=load_data()
    user_data_list=conv_to_list(file_data)
    # check username
    while True:
        if new_username == "":
            print("Username cannot be empty!")
            new_username = input("--Please enter username(Enter b to retun menu): ")
        elif new_username == "b":
            back_to_menu(func_back_to,current_user)
            continue
        username_exists = any(item[1] == new_username for item in user_data_list)
        if username_exists:
            print("Username already exists!")
            new_username = input("--Please enter another username(Enter b to retun menu): ")
        else:
            break
    return new_username


def check_password(new_password,func_back_to,current_user):
    while True:
        if new_password == "":
            print("Password cannot be empty!")
            new_password = input("--Please enter password(Enter b to retun menu): ")
        elif new_password == "b":
            back_to_menu(func_back_to,current_user)
        else:
            break
    return new_password


def approve_user(func_back_to,current_user):
    print("===================================")
    print("           Approve User            ")
    print("===================================")
    print("1. Approved")
    print("2. Reject")
    print("b.back yo menu")

    choice = input("Enter 1 to approve, 2 to reject(Enter b to retun menu): ")
    while choice not in [ "1", "2", "b" ]:
        print("Invalid! Please enter 1, 2 or b")
        choice = input("Enter 1 to approve, 2 to reject(Enter b to retun menu): ")
    if choice == "1":
        return "approved"
    if choice == "2":
        return "reject"
    if choice == "b":
        back_to_menu(func_back_to,current_user)


def user_types(func_back_to,current_user):
    print("==================================")
    print("            User Types            ")
    print("==================================")
    print("1. Customer")
    print("2. Inventory Staff")
    print("3. Admin")
    print("4. SuperUser")
    print("b. back to menu")

    choice = input("Pleace choose user type(Enter b to retun menu): ")
    while choice not in ["1", "2", "3", "4", "b"]:
        choice = input("Invalid user type! Please enter 1, 2, 3 or 4(Enter b to retun menu): ")
    if choice == "1":
        return "customer"
    if choice == "2":
        return "staff"
    if choice == "3":
        return "admin"
    if choice == "4":
        return "superuser"
    if choice == "b":
        back_to_menu(func_back_to,current_user)


def check_name(new_users_name,func_back_to,current_user):
    while True:
        if not new_users_name:
            print("User's name cannot be empty!")
            new_users_name = input("--Please enter a user's name(Enter b to retun menu): ")
        elif new_users_name == "b":
            back_to_menu(func_back_to,current_user)
            continue
        allowed_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz/ ")
        if any(char not in allowed_chars for char in new_users_name):
            print("Invalid name!!")
            new_users_name = input(f"Name must only include alphabet and '/' \n--Please enter user's name(Enter b to retun menu): ")        
        else:
            break

    return new_users_name


def check_phone_no(new_phone_number,func_back_to,current_user):
    while True:
        if new_phone_number =="":
            print("Phone number cannot be empty!")
            new_phone_number = input("--Please enter a phone number(Enter b to retun menu): ")
        elif new_phone_number == "b":
            back_to_menu(func_back_to,current_user)
        elif new_phone_number.isdigit() is False:
            print("Invalid phone number!! \n Phone number must only contain number!!")
            new_phone_number = input("--Please enter another phone number(Enter b to retun menu): ")
        elif len(new_phone_number) not in (10,11):
            print("Invalid phone number!!")
            new_phone_number = input("--Please enter another phone number(Enter b to retun menu): ")
        else:
            break
    return new_phone_number



def check_address(new_user_address,func_back_to,current_user):
    while True:
        if new_user_address =="":
            print("Address cannot be empty!")
            new_user_address = input("--Please re-enter Address(Enter b to retun menu): ")
        elif new_user_address == "b":
            back_to_menu(func_back_to,current_user)
        else:
            break
    return new_user_address


def add_user(func_back_to,current_user):
    #input data
    new_id_number = input("Please enter your IC number(Enter b to retun menu): ")
    new_id_number = check_id(new_id_number,func_back_to,current_user)
    new_username = input("Enter your username(Enter b to retun menu): ")
    new_username = check_username(new_username,func_back_to,current_user)
    new_password = input("Please input a default password(Enter b to retun menu): ")
    new_password = check_password(new_password,func_back_to,current_user)
    new_status = approve_user(func_back_to,current_user)
    new_user_type = user_types(func_back_to,current_user)
    new_users_name = input("Please enter user's name(Enter b to retun menu): ")
    new_users_name = check_name(new_users_name,func_back_to,current_user)
    new_users_phone_no = input("Please enter user's phone number(Enter b to retun menu): ")
    new_users_phone_no = check_phone_no(new_users_phone_no,func_back_to,current_user)
    new_user_address = input("Please enter user's address(Enter b to retun menu): ")
    new_user_address = check_address(new_user_address,func_back_to,current_user)
    #user list
    temp_data_list=[[new_id_number, new_username, new_password, new_status, new_user_type, new_users_name, new_users_phone_no, new_user_address]]
    # add data to the file
    data_to_dict=conv_to_dict(temp_data_list)
    write_data(data_to_dict,"a")

def search_verify_data_admin():
    #get data from users.txt
    file_data=load_data()
    user_data_list=conv_to_list(file_data)
    #search data and add to temp list
    temp_data_list=[]
    for length in range(len(user_data_list)):
        status= user_data_list[length][3]
        user_type=user_data_list[length][4]
        if status=="pending" and user_type=="customer" or user_type=="staff":
            temp_data_list.append(user_data_list[length][:2]+user_data_list[length][3:8]+[length])
    return temp_data_list


def verify_user_admin(func_back_to,current_user):
    #get data from users.txt
    file_data=load_data()
    user_data_list=conv_to_list(file_data)
    temp_data_list=search_verify_data_admin()
    for length in range(len(temp_data_list)):
        print([str(length+1)]+temp_data_list[length][:7])
    item=input("Enter number to select user to verify:")
    while True:
        if item.isdigit() is False:
            item=input("Please enter number to select user to verify:")
        elif int(item) not in [1,len(temp_data_list)]:
            item=input("No user selected! Enter number to select user to verify:")
        else:
            break
    item=int(item)
    item=item-1
    temp_data_list[item][2]=approve_user(func_back_to,current_user)
    edit_item=temp_data_list[item][7]
    #verify the temp_data_list[user]==user_data_list[user]
    if temp_data_list[item][0]==user_data_list[edit_item][0]:
        user_data_list[edit_item][3]=temp_data_list[item][2]
    elif temp_data_list[item][0]!=user_data_list[edit_item][0]:
        for user in user_data_list:
            if temp_data_list[item][0]==user[0]:
                user[3]=temp_data_list[item][2]
    print(temp_data_list[item][:7])
    # write data into user.txt
    data_to_dict=conv_to_dict(user_data_list)
    write_data(data_to_dict,"w")


def search_verify_data_superuser():
    #get data from users.txt
    file_data=load_data()
    user_data_list=conv_to_list(file_data)
    #search data and add to temp list
    temp_data_list=[]
    for length in range(len(user_data_list)):
        status= user_data_list[length][3]
        if status=="pending":
            temp_data_list.append(user_data_list[length][:2]+user_data_list[length][3:8]+[length])
    return temp_data_list

def verify_user_superuser(func_back_to,current_user):
    #get data from users.txt
    file_data=load_data()
    user_data_list=conv_to_list(file_data)
    temp_data_list = search_verify_data_superuser()
    for length in range(len(temp_data_list)):
        print([str(length+1)]+temp_data_list[length][:7])
    item=input("Enter number to select the user to verify:")
    while True:
        if item.isdigit() is False:
            item=input("Please enter number to select user to verify:")
        elif int(item) not in [1,len(temp_data_list)]:
            item=input("No user selected! Enter number to select user to verify:")
        else:
            break
    item=int(item)
    item=item-1
    temp_data_list[item][2]=approve_user(func_back_to,current_user)
    edit_item=temp_data_list[item][7]
    #verify the temp_data_list[user]==user_data_list[user]
    if temp_data_list[item][0]==user_data_list[edit_item][0]:
        user_data_list[edit_item][3]=temp_data_list[item][2]
    elif temp_data_list[item][0]!=user_data_list[edit_item][0]:
        for user in user_data_list:
            if temp_data_list[item][0]==user[0]:
                user[3]=temp_data_list[item][2]
    print(temp_data_list[item][:7])
    # write data into user.txt
    data_to_dict=conv_to_dict(user_data_list)
    write_data(data_to_dict,"w")


def select_and_edit(func_back_to,current_user):
    print("=================================")
    print("     Select the item to edit     ")
    print("=================================")
    print("1. ID Number")
    print("2. Username")
    print("3. Password")
    print("4. Access Status")
    print("5. User Type")
    print("6. Name ")
    print("7. Phone number")
    print("8. address ")
    choice = input("Enter your choice: ")
    while choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("Invalid choice!")
        choice = input("Enter your choice: ")
    if choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        choice = int(choice)
        choice = choice - 1
        updatedata = ""
        if choice == 0:
            updatedata = input("Please enter your IC number(Enter b to retun menu): ")
            updatedata = check_id(updatedata,func_back_to,current_user)
        elif choice == 1:
            updatedata = input("Enter your username(Enter b to retun menu): ")
            updatedata = check_username(updatedata,func_back_to,current_user)
        elif choice == 2:
            updatedata = input("Please input a default password(Enter b to retun menu): ")
            updatedata = check_password(updatedata,func_back_to,current_user)
        elif choice == 3:
            updatedata = approve_user(func_back_to,current_user)
        elif choice == 4:
            updatedata = user_types(func_back_to,current_user)
        elif choice == 5:
            updatedata = input("Please enter user's name(Enter b to retun menu): ")
            updatedata = check_name(updatedata,func_back_to,current_user)
        elif choice == 6:
            updatedata = input("Please enter user's phone number(Enter b to retun menu): ")
            updatedata = check_phone_no(updatedata,func_back_to,current_user)
        elif choice == 7:
            updatedata = input("Please enter user's address(Enter b to retun menu): ")
            updatedata = check_address(updatedata,func_back_to,current_user)
        data=[choice,updatedata]
        return data

def modify_user_details(func_back_to,current_user):
    # get data from users.txt
    file_data=load_data()
    user_data_list=conv_to_list(file_data)
    # print users data
    for length in range(len(user_data_list)):
        print([length+1]+user_data_list[length])
    # select user to modify 
    item=input("Enter number to select the user to modify:")
    while True:
        if item.isdigit() is False:
            item=input("Please enter number to select user to modify:")
        elif int(item) not in range(1,int(len(user_data_list))):
            item=input("No user selected! Enter number to select user to modify:")
        else:
            break
    item=int(item)
    item=item-1
    print(user_data_list[item])
    select_edit = select_and_edit(func_back_to,current_user)
    user_data_list[item][select_edit[0]] = select_edit[1]
    # write data into user.txt
    data_to_dict=conv_to_dict(user_data_list)
    write_data(data_to_dict,"w")

def disable_user_access(func_back_to,current_user):
    #get data from users.txt
    file_data=load_data()
    user_data_list=conv_to_list(file_data)
    #add needed data to temp list
    temp_data_list=[]
    for length in range(len(user_data_list)):
        status= user_data_list[length][3]
        if status=="approved":
            temp_data_list.append(user_data_list[length][:2]+user_data_list[length][3:8]+[length])
    confirm_disable=2
    while confirm_disable==2:
        for length in range(len(temp_data_list)):
            print([length+1]+temp_data_list[length][:7])
        item=input("Enter number to select the user to disable:")
        while True:
            if item.isdigit() is False:
                item=input("Please enter number to select the user to disable:")
            elif int(item) not in [1,len(temp_data_list)]:
                item=input("No user selected! Enter number to select the user to disable: ")
            else:
                break
        item=int(item)
        item=item-1
        print(temp_data_list[item])
        print("Are you sure you wanna disable the user?")
        confirm_disable=input("Enter 1 to disable, enter 2 to re-select(Enter b to retun menu): ")
        while confirm_disable not in ["1","2","b"]:
            confirm_disable=input("Invalid input!! Enter 1 to disable, enter 2 to re-select(Enter b to retun menu): ")
        if confirm_disable=="1":
            temp_data_list[item][2]="disable"
            print(temp_data_list[item])
            edit_item=temp_data_list[item][7]
            #verify the temp_data_list[user]==user_data_list[user]
            if temp_data_list[item][0]==user_data_list[edit_item][1]:
                user_data_list[edit_item][3]=temp_data_list[item][2]
            else:
                for user in user_data_list:
                    if temp_data_list[item][0]==user[0]:
                        user[3]=temp_data_list[item][2]
            data_to_dict=conv_to_dict(user_data_list)
            write_data(data_to_dict,"w")
            print("The user has sucessfully disabled.")
        if confirm_disable=="2":
            disable_user_access()
        if confirm_disable == "b":
            back_to_menu(func_back_to,current_user)
            # add data to the file

def write_user_usage(username, user_type, function):
    from datetime import datetime
    now = datetime.now()
    # Change format to "YYYY-MM-DD HH:MM:SS"
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")  
    log_list = []
    log_list.append([formatted_datetime,username, user_type, function,"\n"])
    with open("user_usage.txt", "a") as user_usage:
        for record in log_list:
            recordString = ",".join(record)
            user_usage.write(recordString)


def show_user_usage():
    with open("user_usage.txt", "r") as user_usage:
        log_list = user_usage.readlines()
        print("\n\n==========================================")
        print("       Inquiry of User system usage       ")
        print("==========================================")
        for record in log_list:
            recordList = record.split(",")
            print(f"{recordList[0]}: {recordList[1]}({recordList[2]})-----{recordList[3]}")

def Check_Customer_Order_Status():
    #get data from users.txt
    with open("orders.txt", "r+") as f:
        data = f.readlines()
        orders_status_list = []
        for record in data:
            record = record.replace(",\n", "")
            evaluated_record = eval(record)
            orders_status_list.append(evaluated_record)
    no=0
    for item in orders_status_list:
        no=no+1
        print(f"{no}. Order ID : {item['order_id']}")
    select_check=input("Which order you wanna check: " )
    select_check=int(select_check)
    while True:
        if select_check =="":
            print("You did not select any order ID. ")
            select_check = input("--Please select another order ID: ")
            select_check=int(select_check)
        elif select_check>len(orders_status_list):
            print("Invalid selection!!")
            select_check = input("--Please enter number to re-select: ")
            select_check=int(select_check)
        else:
            break
    select_check=int(select_check)-1
    item= orders_status_list[select_check]
    print("\n\n==========================================")
    print("           Customer Order Status          ")
    print("==========================================")
    print(f"Order ID : {item['order_id']}")
    print(f"Username : {item['username']}")
    print(f"Status   : {item['status']}")
    print(f"Time     : {item['time']}")
    print(f"Order    : {item['order']}")
    print(f"Send Status : {item['send_status']}")

            
def report():
    with open("user_usage.txt", "r") as user_usage:
        usage_list = user_usage.readlines()
        user_usage_list=[]
        for usage in usage_list:
            user_usage_list.append(usage.split(","))
    # set to defalt report list
    report_list=[["order_product",0],
                 ["service_repair",0],
                 ["modify_request",0],
                 ["order_status",0],
                 ["customer_reports",0],
                 ["add_user",0],
                 ["verify_new_user(superuser)",0],
                 ["verify_new_customers",0],
                 ["modify_user_personal_details",0],
                 ["disable_user_access",0],
                 ["inquiry_of_user's_system_usage",0],
                 ["stock_purchase_order_status(admin/superuser)",0],
                 ["check_customer_order_status",0],
                 ["user_management_report",0],
                 ["add_or_update_inventory",0],
                 ["check_stock",0],
                 ["adjust_stock",0],
                 ["create_purchase_order",0],
                 ["modify_purchase_order",0],
                 ["cancel_purchase_order",0],
                 ["purchase_order_status",0],
                 ["inventory_report",0],
                 ["change_customer_order_status",0],
                 ["exit",0]
                 ]

    # Calculate the usage
    for item in user_usage_list:
        report_list[0][1]
        if item[3] == report_list[0][0]:
            report_list[0][1]+=1
        elif item[3] == report_list[1][0]:
            report_list[1][1]+=1
        elif item[3] == report_list[2][0]:
            report_list[2][1]+=1
        elif item[3] == report_list[3][0]:
            report_list[3][1]+=1
        elif item[3] == report_list[4][0]:
            report_list[4][1]+=1
        elif item[3] == report_list[5][0]:
            report_list[5][1]+=1
        elif item[3] == report_list[6][0]:
            report_list[6][1]+=1
        elif item[3] == report_list[7][0]:
            report_list[7][1]+=1
        elif item[3] == report_list[8][0]:
            report_list[8][1]+=1
        elif item[3] == report_list[9][0]:
            report_list[9][1]+=1
        elif item[3] == report_list[10][0]:
            report_list[10][1]+=1
        elif item[3] == report_list[11][0]:
            report_list[11][1]+=1
        elif item[3] == report_list[12][0]:
            report_list[12][1]+=1
        elif item[3] == report_list[13][0]:
            report_list[13][1]+=1
        elif item[3] == report_list[14][0]:
            report_list[14][1]+=1
        elif item[3] == report_list[15][0]:
            report_list[15][1]+=1
        elif item[3] == report_list[16][0]:
            report_list[16][1]+=1
        elif item[3] == report_list[17][0]:
            report_list[17][1]+=1
        elif item[3] == report_list[18][0]:
            report_list[12][1]+=1
        elif item[3] == report_list[19][0]:
            report_list[19][1]+=1
        elif item[3] == report_list[20][0]:
            report_list[20][1]+=1
        elif item[3] == report_list[21][0]:
            report_list[21][1]+=1
        elif item[3] == report_list[22][0]:
            report_list[22][1]+=1
        elif item[3] == report_list[23][0]:
            report_list[23][1]+=1

    print("\n\n")
    print("="*50)
    print("Report".center(50))
    print("="*50)
    for item in report_list:
        print(f"{item[0].center(45)}|  {item[1]}\n{"-"*45}|{"-"*5}")


def back_to_menu(run_function,current_user):
    return_menu=input("Please remain empty to retun menu: ")
    while True:
        if return_menu=="":
            run_function(current_user)
        else:
            break


def inventory_order_status():
    purchase_orders = []
    with open("INVENTORY_DATA.TXT", "r") as f:
        lines = f.readlines()
        section = None
        for line in lines:
            line = line.strip()
            if line == "Purchase Orders:":
                section = "purchase_orders"
            elif line and section == "purchase_orders":
                    order_id, details = line.split(": ")
                    item_name, quantity, price, status = details.split(", ")
                    inventory=[order_id , item_name , quantity , price , status]
                    purchase_orders.append(inventory)

    print("\n\n")
    print("="*68)
    print("Inventory Order Status".center(68))
    print("="*68)
    # Print headers
    print(f"{'Order ID':<10}{'Item Name':<20}{'Quantity':<10}{'Price(RM)':<12}{'Status':<12}")
    for item in purchase_orders:
        print(f"{item[0].center(9):<10}{item[1]:<20}{str(item[2]).center(8):<10}{str(item[3]).center(9):<12}{item[4]:<12}")


def user_mangement_menu_superuser(current_user):
    current_user=current_user
    print("\n\n===================================")
    print("          User Management          ")
    print("===================================")
    print("1. Add User")
    waiting=len(search_verify_data_superuser())
    print(f"2. Verify New User (Waiting for verify: {str(waiting)})")
    print("3. Modify User Personal Details")
    print("4. Disable User Access")
    print("5. Inquiry of User's system usage ")
    print("6. Check Customer Order Status ")
    print("7. Stock Purchase Order Status")
    print("8. User Management Reports ")
    print("9. Exit ")
    choice = input("\nPlease enter 1 to 9 to continue: ")

    while choice not in ["1","2","3","4","5","6","7","8","9"]:
        print("\n\n===================================")
        print("          User Management          ")
        print("===================================")
        print("1. Add User")
        waiting=len(search_verify_data_superuser())
        print(f"2. Verify New User (Waiting for verify: {str(waiting)})")
        print("3. Modify User Personal Details")
        print("4. Disable User Access")
        print("5. Inquiry of User's system usage ")
        print("6. Check Customer Order Status ")
        print("7. Stock Purchase Order Status")
        print("8. User Management Reports ")
        print("9. Exit ")
        print("\nInvalid choice!!")
        choice = input("Please enter 1 to 9 to select the function: ")
    if choice=="1":
        add_user(func_back_to=user_mangement_menu_superuser,current_user=current_user)
        write_user_usage(current_user[1],current_user[4], "add_user")
        back_to_menu(user_mangement_menu_superuser,current_user=current_user)
    if choice=="2":
        if waiting == 0:
            print("There is no user waiting to be verify.")
            back_to_menu(user_mangement_menu_superuser,current_user=current_user)
        else:
            verify_user_superuser(func_back_to=user_mangement_menu_superuser,current_user=current_user)
            write_user_usage(current_user[1],current_user[4], "verify_new_user(superuser)")
            back_to_menu(user_mangement_menu_superuser,current_user=current_user)
    if choice=="3":
        modify_user_details(func_back_to=user_mangement_menu_superuser,current_user=current_user)
        write_user_usage(current_user[1],current_user[4], "modify_user_personal_details")
        back_to_menu(user_mangement_menu_superuser,current_user=current_user)
    if choice=="4":
        disable_user_access(func_back_to=user_mangement_menu_superuser,current_user=current_user)
        write_user_usage(current_user[1],current_user[4], "disable_user_access")
        back_to_menu(user_mangement_menu_superuser,current_user=current_user)
    if choice=="5":
        write_user_usage(current_user[1],current_user[4], "inquiry_of_user's_system_usage")
        show_user_usage()
        back_to_menu(user_mangement_menu_superuser,current_user=current_user)
    if choice=="6":
        Check_Customer_Order_Status()
        back_to_menu(user_mangement_menu_superuser,current_user=current_user)
    if choice=="7":
        inventory_order_status()
        write_user_usage(current_user[1],current_user[4], "stock_purchase_order_status(admin/superuser)")
        back_to_menu(user_mangement_menu_superuser,current_user=current_user)
    if choice=="8":
        write_user_usage(current_user[1],current_user[4], "user_management_report")
        report()
        back_to_menu(user_mangement_menu_superuser,current_user=current_user)
    if choice=="9":
        write_user_usage(current_user[1],current_user[4], "exit")
        exit()
        

def user_mangement_menu_admin(current_user):
    current_user=current_user
    print("===================================")
    print("          User Management          ")
    print("===================================")
    waiting=len(search_verify_data_admin())
    print( f"1. Verify New Customer (Waiting for verify: {str(waiting)})")
    print("2. Check Customer Order Status")
    print("3. Stock Purchase Order Status")
    print("4. User Management Reports ")
    print("5. Exit ")
    choice = input("\nPlease enter 1 to 5 to continue: ")

    while choice not in ["1", "2", "3", "4", "5"]:
        print("===================================")
        print("          User Management          ")
        print("===================================")
        waiting=len(search_verify_data_admin())
        print( f"1. Verify New Customer (Waiting for verify: {str(waiting)})")
        print("2. Check Customer Order Status")
        print("3. Stock Purchase Order Status")
        print("4. User Management Reports ")
        print("5. Exit ")
        print("\nInvalid choice!")
        choice = input("Please enter 1 to 5 to continue: ")
    if choice=="1":
        if waiting == 0:
            print("There is no customers waiting to be verify.")
            back_to_menu(user_mangement_menu_admin,current_user)
        else:
            verify_user_admin(func_back_to=user_mangement_menu_admin,current_user=current_user)
            write_user_usage(current_user[1],current_user[4], "verify_new_customers")
            back_to_menu(user_mangement_menu_admin,current_user)
    if choice=="2":
        Check_Customer_Order_Status()
        back_to_menu(user_mangement_menu_admin,current_user)
    if choice=="3":
        inventory_order_status()
        write_user_usage(current_user[1],current_user[4], "stock_purchase_order_status(admin/superuser)")
        back_to_menu(user_mangement_menu_admin,current_user)
    if choice=="4":
        write_user_usage(current_user[1],current_user[4], "user_management_report")
        report()
        back_to_menu(user_mangement_menu_admin,current_user)
    if choice=="5":
        write_user_usage(current_user[1],current_user[4], "exit")
        exit()
        
