def distance(num1, num2, num3):
    condition1 = (abs(num1 - num2) <= 1) and (abs(num1 - num3) >= 2) and (abs(num2 - num3) >= 2)
    condition2 = (abs(num1 - num3) <= 1) and (abs(num1 - num2) >= 2) and (abs(num2 - num3) >= 2)
    return condition1 or condition2


def main():
    print(distance(1, 2, 10)) # True
    print(distance(4, 5, 3)) # False


if __name__ == "__main__":
    main()