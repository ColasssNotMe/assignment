from crud import update_user, delete_user, read_user
from order_pages import page1, page2, page3
# product[0] = product name
# product[1] = product price


def customer_menu():
    print("===================================")
    print("               Menu                ")
    print("===================================")
    print("1. Order product")
    print("2. Service / Repair")
    print("3. Modify request")
    print("4. Order status")
    print("5. Reports")
    selection = int(input("Enter your selection: "))
    while selection not in [1, 2, 3, 4]:
        print("Invalid selection!")
        selection = int(input("Enter your selection: "))
    if selection == 1:
        order_product(current_page=1)
    elif selection == 2:
        service_repair()
    elif selection == 3:
        modify_request()
    elif selection == 4:
        order_status()
    elif selection == 5:
        reports()


def order_product(current_page):
    all_product = []
    current_order_list = []
    current_page_product = []
    with open("orders.txt", "a") as f:
        pass
        f.close()
    print("===================================")
    print("              Product              ")
    print("===================================")

    # TODO: need to pei he other user
    # read the product from text file
    with open("products.txt", "r") as f:
        data = f.readlines()
        for product in data:
            product_list = product.split(",")
            all_product.append(product_list)
        f.close()

    # len_shown_product : to know how many product shown in the page
    # current_order_list : to store the product that user want to order
    if current_page == 1:
        len_shown_product, current_page_product = page1(all_product=all_product)
        current_order_list = user_selection_order_product(
            current_order_list=current_order_list,
            length=len_shown_product,
            current_page_product=current_page_product,
        )
    elif current_page == 2:
        if len(all_product) > 5:
            len_shown_product, current_page_product = page2(all_product=all_product)
        else:
            len_shown_product, current_page_product = page1(all_product=all_product)
        current_order_list = user_selection_order_product(
            current_order_list=current_order_list,
            length=len_shown_product,
            current_page_product=current_page_product,
        )
    elif current_page == 3:
        if len(all_product) > 5:
            len_shown_product, current_page_product = page3(all_product=all_product)
        else:
            len_shown_product, current_page_product = page2(all_product=all_product)
        current_order_list = user_selection_order_product(
            current_order_list=current_order_list,
            length=len_shown_product,
            current_page_product=current_page_product,
        )


def user_selection_order_product(current_order_list, length, current_page_product):
    selection = input("Enter the product name you want to order: ")

    # check for shown product len to prevent index error
    # what this append?
    if int(selection) <= length or selection in ["p1", "p2", "p3"]:
        if selection == ["1", "2", "3", "4", "5"]:
            current_order_list.append(current_page_product[int(selection) - 1])
        elif selection in ["p1", "p2", "p3"]:
            order_product(current_page=selection[1])

    else:
        print("Invalid selection!")
        selection = int(input("Enter your selection: "))
    return current_order_list


# TODO: change file name


def service_repair():
    pass


def modify_request():
    pass


def order_status():
    pass


def reports():
    pass
