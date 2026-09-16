def is_greater(my_list, n):
    """

    :param my_list: A list of numbers
    :param n: A number ( integer )
    :return: A list of the numbers in my_list that are greater than n
    """
    result_list = []
    index = 0

    while index < len(my_list):
        if my_list[index] > n:
            result_list.append(my_list[index])
        index += 1

    return result_list