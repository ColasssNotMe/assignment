def process_dictionary(inventory):
    """convert dictionary from inventory to list

    Args:
        inventory (dict): inventory dictionary

    Returns:
        list: list of inventory
    """
    inventory_list = []
    for key, value in inventory.items():
        inventory_list.append([key, value])
    return inventory_list


def page1(inventory):
    inventory_list = process_dictionary(inventory)
    counter = 1
    current_page_product = inventory_list[0:5]
    # show only 5 product per page
    # print only the product name
    # if the thing too repetitive, can use function (elif part)
    for product in inventory_list:
        print(f"{counter}. {product[0]}")
        counter += 1
    print("p2. Page 2")
    print("p3. Page 3")
    print("c. Complete order")
    print("b. Back to main menu")

    return len(current_page_product), current_page_product


def page2(inventory):
    inventory_list = process_dictionary(inventory)
    counter = 1
    current_page_product = inventory_list[5:10]
    for product in inventory_list[5:]:
        print(f"{counter}. {product[0]}")
        counter += 1

    print("p1. Page 1")
    print("p3. Page 3")
    print("c. Complete order")
    print("b. Back to main menu")
    return len(current_page_product), current_page_product


def page3(inventory):
    inventory_list = process_dictionary(inventory)
    counter = 1
    current_page_product = inventory_list[10:15]
    for product in inventory_list[10:]:
        print(f"{counter}. {product[0]}")
        counter += 1
    print("p1. Page 1")
    print("p2. Page 2")
    print("c. Complete order")
    print("b. Back to main menu")
    return len(current_page_product), current_page_product
