def are_lists_equal(list1, list2):
    """

    :param list1: List containing numbers that can be integers and float
    :param list2: List containing numbers that can be integers and float
    :return: A boolean indicating whether list1 and list2 are equal
    """
    return sorted(list1) == sorted(list2)


def main():
    list1 = [0.6, 1, 2, 3]
    list2 = [3, 2, 0.6, 1]
    list3 = [9, 0, 5, 10.5]

    print(f"list1 == list2 ? {are_lists_equal(list1, list2)}")
    print(f"list1 == list3 ?  {are_lists_equal(list1, list3)}")


if __name__ == "__main__":
    main()