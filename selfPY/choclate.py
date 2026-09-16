def chocolate_maker(small, big, x):
    """

    :param small: amount of small chocolate pieces
    :param big: amount of big chocolate pieces
    :param x: desired length of choclate
    :return: Boolean variable that represent the ability to create a line of chocolates of the desired length
    """
    if big * 5 + small < x:
        return False

    max_big_to_use = x // 5
    actual_big_used = min(big, max_big_to_use)
    remaining_length = x - (actual_big_used * 5)

    if small >= remaining_length:
        return True
    else:
        return False
def main():
    print(chocolate_maker(3, 1, 8))  # Output: True
    print(chocolate_maker(3, 1, 9))  # Output: False
    print(chocolate_maker(3, 2, 10))  # Output: True


if __name__ == "__main__":
    main()