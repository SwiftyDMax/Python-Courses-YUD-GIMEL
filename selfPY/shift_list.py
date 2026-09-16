def shift_left(my_list):
    """

    :param my_list: Any list
    :return: The list shifted to the left by 1
    """
    return my_list[1:] + my_list[:1]


def main():
    numbers = [1, 2, 3, 4, 5]
    shifted_numbers = shift_left(numbers)
    print(f"Original: {numbers}")
    print(f"Shifted:  {shifted_numbers}\n")

    words = ["apple", "banana", "cherry"]
    shifted_words = shift_left(words)
    print(f"Original: {words}")
    print(f"Shifted:  {shifted_words}\n")




if __name__ == "__main__":
    main()