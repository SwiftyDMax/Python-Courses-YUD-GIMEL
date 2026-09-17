def print_products(products):
    print(products)


def count_products(products):
    print(len(products))


def is_product_in_list(products):
    product = input("Enter product name: ")
    print(product in products)


def count_product_instances(products):
    product = input("Enter product name: ")
    print(products.count(product))


def remove_product(products):
    product = input("Enter product name: ")
    if product in products:
        products.remove(product)


def add_product(products):
    product = input("Enter product name: ")
    products.append(product)


def print_invalid_products(products):
    invalid_products = []
    for p in products:
        if len(p) < 3 or not p.isalpha():
            invalid_products.append(p)
    print(invalid_products)


def remove_duplicates(products):
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