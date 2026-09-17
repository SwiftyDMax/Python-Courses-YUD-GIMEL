def print_products(products):
    """
    Print out the products in the list

    :param products: A list of product names
    :return: None
    """
    print(products)


def count_products(products):
    """
    Count and print the total number of products in the list

    :param products: A list of product names
    :return: None
    """
    print(len(products))


def is_product_in_list(products):
    """
    Request a product name and check if it is in the list

    :param products: A list of product names
    :return: None
    """
    product = input("Enter product name: ")
    print(product in products)


def count_product_instances(products):
    """
    Request a product name and count the number of instances in the list

    :param products: A list of product names
    :return: None
    """
    product = input("Enter product name: ")
    print(products.count(product))


def remove_product(products):
    """
    Request a product name and remove it from the list

    :param products: A list of product names
    :return: None
    """
    product = input("Enter product name: ")
    if product in products:
        products.remove(product)


def add_product(products):
    """
    Request a product name and add it to the list

    :param products: A list of product names
    :return: None
    """
    product = input("Enter product name: ")
    products.append(product)


def print_invalid_products(products):
    """
    Identify and print invalid products

    :param products: A list of product names
    :return: None
    """
    invalid_products = []
    for p in products:
        if len(p) < 3 or not p.isalpha():
            invalid_products.append(p)
    print(invalid_products)


def remove_duplicates(products):
    """
    Remove duplicate products

    :param products: A list of product names
    :return: None
    """
    unique_products = []
    for item in products:
        if item not in unique_products:
            unique_products.append(item)
    products.clear()
    products.extend(unique_products)


def main():

    raw_input = input("Enter shopping list (comma-separated): ")
    products = raw_input.split(",")

    choice = 0
    while choice != 9:
        choice = int(input("Enter choice (1-9): "))

        if choice == 1:
            print_products(products)
        elif choice == 2:
            count_products(products)
        elif choice == 3:
            is_product_in_list(products)
        elif choice == 4:
            count_product_instances(products)
        elif choice == 5:
            remove_product(products)
        elif choice == 6:
            add_product(products)
        elif choice == 7:
            print_invalid_products(products)
        elif choice == 8:
            remove_duplicates(products)


if __name__ == "__main__":
    main()