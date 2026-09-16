def fix_age(age):
    """

    :param age:
    :return: fixed age, teens are filtered out except for ages 15 and 16
    """
    if 13 <= age <= 19 and age != 15 and age != 16:
        return 0
    return age

def filter_teens(a=13, b=13, c=13):
    """

    :param a: age
    :param b: age
    :param c: age
    :return:  sum of 3 ages fixed
    """
    return fix_age(a) + fix_age(b) + fix_age(c)


def main():
    print(filter_teens())  # Output: 0
    print(filter_teens(1, 2, 3))  # Output: 6
    print(filter_teens(2, 13, 1))  # Output: 3
    print(filter_teens(2, 1, 15))  # Output: 18


if __name__ == "__main__":
    main()