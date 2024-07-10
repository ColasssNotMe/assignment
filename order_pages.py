def page1(all_product):
    counter = 1
    current_page_product = all_product[0:5]
    # show only 5 product per page
    # print only the product name
    # if the thing too repetitive, can use function (elif part)
    for product in all_product:
        print(f"{counter}. {product[0]}")
        counter += 1
        if counter > 5:
            print("p2. Page 2")
            print("p3. Page 3")
            print("c. Complete order")
            print("b. Back to main menu")
            break
    return len(current_page_product), current_page_product


def page2(all_product):
    counter = 1
    current_page_product = all_product[5:10]
    for product in all_product[5:]:
        print(f"{counter}. {product[0]}")
        counter += 1
        if counter > 5:
            print("p1. Page 1")
            print("p3. Page 3")
            print("c. Complete order")
            print("b. Back to main menu")
            break
    return len(current_page_product), current_page_product


def page3(all_product):
    counter = 1
    current_page_product = all_product[10:15]
    for product in all_product[10:]:
        print(f"{counter}. {product[0]}")
        counter += 1
        if counter > 5:
            print("p1. Page 1")
            print("p2. Page 2")
            print("c. Complete order")
            print("b. Back to main menu")
            break
    return len(current_page_product), current_page_product
