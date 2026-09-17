def numbers_letters_count(my_str):
    """

    :param my_str: string
    :return A list with two variables in it, the first represents amount of digits and the second represents amount of letters
    """
    digits_count = 0
    letters_count = 0

    for char in my_str:
        if char.isdigit():
            digits_count += 1
        else:
            letters_count += 1

    return [digits_count, letters_count]


def main():
    print(numbers_letters_count("Python 3.6.3"))


if __name__ == "__main__":
    main()