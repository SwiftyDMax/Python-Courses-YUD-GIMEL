def format_list(my_list):
    """

    :param my_list: A list of strings
    :return: a string fromatted this way : the value of each even index seperated by , and the last index of the list added with the word and seperating them
    """
    if not my_list:
        return ""
    if len(my_list) == 1:
        return my_list[0]
    every_other = my_list[:-1:1]
    return ", ".join(every_other) + ", and " + my_list[-1]


def main():
    sample_list = ["apple", "banana", "cherry", "date", "elderberry"]

    result = format_list(sample_list)
    print(f"Original list: {sample_list}")
    print(f"Formatted:     {result}")


if __name__ == "__main__":
    main()