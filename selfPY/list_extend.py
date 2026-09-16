def extend_list_x(list_x, list_y):
    """

    :param list_x: A list of numbers
    :param list_y: A list of numbers
    :return: The extended list
    """
    list_x[:0] = list_y
    return list_x


def main():
    x = [4, 5, 6]
    y = [1, 2, 3]

    print(f"Before : x = {x}, y = {y}")

    result = extend_list_x(x, y)

    print(f"Result :  {result}")



if __name__ == "__main__":
    main()