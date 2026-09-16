def longest(my_list):
    print(sorted(my_list, key=len))
    return sorted(my_list)[-1]


def main():
    list1 = ["111", "234", "2000", "goru", "birthday", "09"]

    result = longest(list1)

    print(f"List: {list1}")
    print(f"Longest string: {result}")


if __name__ == "__main__":
    main()