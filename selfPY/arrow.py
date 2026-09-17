def arrow(my_char, max_length):
    """

    :param my_char: char that will be printed
    :param max_length: The maximum length we will reach when printing
    :return: None
    """
    for i in range(max_length + 1):
        print(my_char * i)
    for i in range(1,max_length):
        print(my_char * (max_length-i))


def main():
    arrow('*', 5)


if __name__ == "__main__":
    main()