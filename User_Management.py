#from inventory import menu

def approve_user():
    print("===================================")
    print("           Approve User            ")
    print("===================================")
    print("1. Approved")
    print("2. Reject")

    choice = int(input("Enter 1 to approve, 2 to reject: "))
    while choice not in [1, 2]:
        print("Invalid! Please enter 1 or 2")
        choice = int(input("Enter 1 to approve, 2 to reject: "))
    if choice==1:
        return "approved"
    if choice==2:
        return "reject"

def user_types():
    print("==================================")
    print("            User Types            ")
    print("==================================")
    print("1. Customer")
    print("2. Inventory Staff")
    print("3. Admin")
    print("4. SuperUser")

    choice = int(input("Enter user type: "))
    while choice not in [1, 2, 3, 4]:
        choice = int(input("Invalid user type! Please enter 1, 2, 3 or 4: "))
    if choice==1:
        return "customer"
    if choice==2:
        return "staff"
    if choice==3:
        return "admin"
    if choice==4:
        return "superuser"

def add_user():
    #input data
    id_number=input("Please input IC/passport number: ")
    username=input("Please input username: ")
    password=input("Please input a defult password: ")
    status=approve_user()
    user_type=user_types()
    users_name=input("Please enter user's name: ")
    users_phone_no=input("Please enter user's phone number: ")
    user_email=input("Please enter user's email: ")
    #user list
    temp_data_list=[id_number, username, password, status, user_type, users_name, users_phone_no, user_email, "\n"]
    # add data to the file
    with open("users.txt", "a") as f:
        new_formatted=",".join(temp_data_list)
        f.write(new_formatted)


def verify_user_admin():
    #get data from users.txt
    with open("users.txt", "r") as user_data:
        data_list = user_data.readlines()
        user_data_list=[]
        for data in data_list:
            user_data_list.append(data.split(","))
    #add to temp list
    temp_data_list=[]
    for length in range(len(user_data_list)):
        status= user_data_list[length][3]
        user_type=user_data_list[length][4]
        if status=="pending" and user_type=="customer" or user_type=="staff":
            temp_data_list.append(user_data_list[length][:2]+user_data_list[length][3:8]+[length])
    for length in range(len(temp_data_list)):
        print([str(length+1)]+temp_data_list[length][:7])
    item=int(input("Enter number to select the user to verify:"))
    while item>len(temp_data_list):
        item=int(input("No user selected! Enter number to select the user to verify:"))
    if item<=len(temp_data_list):
        item=item-1
        temp_data_list[item][2]=approve_user()
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
    with open("users.txt", "w") as f:
        for record in user_data_list:
            recordString = ",".join(record)
            f.write(recordString)


def verify_user_superuser():
    #get data from users.txt
    with open("users.txt", "r") as user_data:
        data_list = user_data.readlines()
        user_data_list=[]
        for data in data_list:
            user_data_list.append(data.split(","))
    #add needed data to temp list
    temp_data_list=[]
    for length in range(len(user_data_list)):
        status= user_data_list[length][3]
        if status=="pending":
            temp_data_list.append(user_data_list[length][:2]+user_data_list[length][3:8]+[length])
    for length in range(len(temp_data_list)):
        print([str(length+1)]+temp_data_list[length][:7])
    item=int(input("Enter number to select the user to verify:"))
    while item>len(temp_data_list):
        item=int(input("No user selected! Enter number to select the user to verify:"))
    if item<=len(temp_data_list):
        item=item-1
        temp_data_list[item][2]=approve_user()
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
    with open("users.txt", "w") as f:
        for record in user_data_list:
            recordString = ",".join(record)
            f.write(recordString)


def select_item_edit():
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
    print("8. Email ")
    choice = int(input("Enter your choice: "))
    while choice not in [1, 2, 3, 4, 5, 6, 7, 8]:
        print("Invalid choice!")
        choice = int(input("Enter your choice: "))
    if choice in [1, 2, 3, 4, 5, 6, 7, 8]:
        choice=choice-1
        return choice

def modify_user_details():
    # get data from users.txt
    with open("users.txt", "r") as user_data:
        data_list = user_data.readlines()
        user_data_list=[]
        for data in data_list:
            user_data_list.append(data.split(","))
    # print users data
    for length in range(len(user_data_list)):
        print([length+1]+user_data_list[length])
    # select user to modify 
    item=int(input("Enter number to select the user to verify:"))
    while item>len(user_data_list):
        item=int(input("No user selected! Enter number to select the user to verify:"))
    if item<=len(user_data_list):
        item=item-1
        print(user_data_list[item])
        edit_item=select_item_edit()
        new_item=input("What is the new up date?:")
        user_data_list[item][edit_item]=new_item
    # write data into user.txt
    with open("users.txt", "w") as f:
        for record in user_data_list:
            recordString = ",".join(record)
            f.write(recordString)

def disable_user_access():
    #get data from users.txt
    with open("users.txt", "r") as user_data:
        data_list = user_data.readlines()
        user_data_list=[]
        for data in data_list:
            user_data_list.append(data.split(","))
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
        item=int(input("Enter number to select the user to disable:"))
        while item>len(temp_data_list):
            item=int(input("No user selected! Enter number to select the user to disable:"))
        if item<=len(temp_data_list):
            item=item-1
            print(temp_data_list[item])
            print("Are you sure you wanna disable the user?")
            confirm_disable=int(input("Enter 1 to disable, enter 2 to re-select: "))
            if confirm_disable==1:
                temp_data_list[item][2]="disable"
                print(temp_data_list[item])
                edit_item=temp_data_list[item][7]
                #verify the temp_data_list[user]==user_data_list[user]
                if temp_data_list[item][0]==user_data_list[edit_item][0]:
                    print("true")
                    user_data_list[edit_item][3]=temp_data_list[item][2]
                elif temp_data_list[item][0]!=user_data_list[edit_item][0]:
                    print("false")
                    for user in user_data_list:
                        if temp_data_list[item][0]==user[0]:
                            user[3]=temp_data_list[item][2]
                # add data to the file
                with open("users.txt", "w") as f:
                    for record in user_data_list:
                        recordString = ",".join(record)
                        f.write(recordString)
                print("The user has sucessfully disabled.")

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
        print("==========================================")
        print("       Inquiry of User system usage       ")
        print("==========================================")
        for record in log_list:
            recordList = record.split(",")
            print(f"{recordList[0]}: {recordList[1]}({recordList[2]})-----{recordList[3]}\n")


def report():
    with open("user_usage.txt", "r") as user_usage:
        usage_list = user_usage.readlines()
        user_usage_list=[]
        for usage in usage_list:
            user_usage_list.append(usage.split(","))
    # set to defalt 0
    no_order_product=0
    no_service_repair=0
    no_modify_request=0
    no_order_status=0
    no_customer_reports=0
    no_verify_new_admin_or_customers=0
    no_verify_new_customers=0
    no_modify_user_personal_details=0
    no_disable_user_access=0
    no_inquiry_of_users_system_usage=0
    no_inventory_menu=0
    no_check_customer_order_status=0
    no_create_purchase_order=0
    no_modify_purchase_order=0
    no_cancel_purchase_order=0
    no_perchase_order_status=0
    no_inventory_report=0
    # Calculate the usage
    for item in user_usage_list:
        if item[3] == "order_product":
            no_order_product+=1
        elif item[3] == "service_repair":
            no_service_repair+=1
        elif item[3] == "modify_request":
            no_modify_request+=1
        elif item[3] == "order_status":
            no_order_status+=1
        elif item[3] == "customer_reports":
            no_customer_reports+=1
        elif item[3] == "add_user":
            no_add_user=no_add_user+1
        elif item[3] == "verify_new_admin_or_customers":
            no_verify_new_admin_or_customers+=1
        elif item[3] == "verify_new_customers":
            no_verify_new_customers+=1
        elif item[3] == "modify_user_personal_details":
            no_modify_user_personal_details+=1
        elif item[3] == "disable_user_access":
            no_disable_user_access+=1
        elif item[3] == "inquiry_of_user's_system_usage":
            no_inquiry_of_users_system_usage+=1
        elif item[3] == "inventory_menu":
            no_inventory_menu+=1
        elif item[3] == "check_customer_order_status":
            no_check_customer_order_status+=1
        elif item[3] == "user_management_report":
            no_user_management_report=no_user_management_report+1
        elif item[3] == "add_or_update_inventory":
            no_add_or_update_inventory=no_add_or_update_inventory+1
        elif item[3] == "check_stock":
            no_check_stock=no_check_stock+1
        elif item[3] == "adjust_stock":
            no_adjust_stock=no_adjust_stock+1
        elif item[3] == "create_purchase_order":
            no_create_purchase_order+=1
        elif item[3] == "modify_purchase_order":
            no_modify_purchase_order+=1
        elif item[3] == "cancel_purchase_order":
            no_cancel_purchase_order+=1
        elif item[3] == "purchase_order_status":
            no_perchase_order_status+=1
        elif item[3] == "inventory_report":
            no_inventory_report+=1
    print("==========================================")
    print("                 Report                   ")
    print("==========================================")
    print(f"Order product: {no_order_product}")
    print(f"Service repair: {no_service_repair}")
    print(f"Modify request: {no_modify_request}")
    print(f"Order status: {no_order_status}")
    print(f"Customer reports: {no_customer_reports}")
    print(f"Verify new admin or customers account(Superuser): {no_verify_new_admin_or_customers}")
    print(f"Verify new customers account(admin): {no_verify_new_customers}")
    print(f"Modify user's personal details: {no_modify_user_personal_details}")
    print(f"Disable user's access: {no_disable_user_access}")
    print(f"Inquiry of user's system usage: {no_inquiry_of_users_system_usage}")
    print(f"Check customer order status: {no_check_customer_order_status}")
    print(f"Create Purchase Order: {no_create_purchase_order}")
    print(f"Modify Purchase Order:{no_modify_purchase_order}")
    print(f"Cancel Purchase Order: {no_cancel_purchase_order}")
    print(f"Perchase Order Status{no_perchase_order_status}")
    print(f"Inventory Report: {no_inventory_report}")


def user_mangement_menu_superuser(current_user):
    current_user=current_user
    print("===================================")
    print("          User Management          ")
    print("===================================")
    print("1. Add User")
    print("2. Verify New Admin Or Customers ")
    print("3. Modify User Personal Details")
    print("4. Disable User Access")
    print("5. Inquiry of User's system usage ")
    print("6. Check Customer Order Status ")
    print("7. Inventory Menu")
    print("8. User Management Reports ")
    choice = int(input("Enter your choice: "))

    while choice not in [1, 2, 3, 4, 5, 6, 7, 8]:
        print("Invalid choice!")
        choice = int(input("Enter your choice: "))
    if choice==1:
        add_user()
        write_user_usage(current_user[1],current_user[4], "add_user")
    if choice==2:
        verify_user_superuser()
        write_user_usage(current_user[1],current_user[4], "verify_new_admin_or_customers")
    if choice==3:
        modify_user_details()
        write_user_usage(current_user[1],current_user[4], "modify_user_personal_details")
    if choice==4:
        disable_user_access()
        write_user_usage(current_user[1],current_user[4], "disable_user_access")
    if choice==5:
        write_user_usage(current_user[1],current_user[4], "inquiry_of_user's_system_usage")
        show_user_usage()
    if choice==6:
        pass
    if choice==7:
        #import from zhiming function
        menu()
        write_user_usage(current_user[1],current_user[4], "inventory_menu")
    if choice==8:
        report()
        write_user_usage(current_user[1],current_user[4], "user_management_report")

def user_mangement_menu_admin(current_user):
    current_user=current_user
    print("===================================")
    print("          User Management          ")
    print("===================================")
    print("1. Verify New Customers")
    print("2. Check Customer Order Status")
    print("3. Inventory Menu")
    print("4. User Management Reports ")

    choice = int(input("Enter your choice: "))
    while choice not in [1, 2, 3, 4]:
        print("Invalid choice!")
        choice = int(input("Enter your choice: "))
    if choice==1:
        verify_user_admin()
        write_user_usage(current_user[1],current_user[4], "verify_new_customers")
    if choice==2:
        pass
    if choice==3:
        pass
    if choice==4:
        report()
        write_user_usage(current_user[1],current_user[4], "user_management_report")

current_user=["00000000000000", "Ah Huat", "Huat AH", "approved", "admin", "Huat Ah Bing", "0123456789", "123456abc@gmail.com", "\n"]
user_mangement_menu_admin(current_user)