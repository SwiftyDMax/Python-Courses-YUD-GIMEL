def seven_boom(end_number):
    """Generates a list from 0 to end_number, replacing numbers divisible by 7
    or containing the digit '7' with 'BOOM'.

    :param end_number: The limit of the range.
    :return: A list of numbers and 'BOOM' strings.
    """
    result = []
    for num in range(end_number + 1):
        if num % 7 == 0 or '7' in str(num):
            result.append('BOOM')
        else:
            result.append(num)
    return result


def main():
    print(seven_boom(17))


if __name__ == "__main__":
    main()