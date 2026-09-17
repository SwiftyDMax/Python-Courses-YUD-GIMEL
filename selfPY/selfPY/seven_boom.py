def seven_boom(end_number):
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