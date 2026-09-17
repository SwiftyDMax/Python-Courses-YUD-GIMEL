def sequence_del(my_str):
    if not my_str:
        return ""

    result = [my_str[0]]
    for char in my_str[1:]:
        if char != result[-1]:
            result.append(char)

    return "".join(result)


def main():
    print(sequence_del("ppyyyyythhhhhooonnnnn"))
    print(sequence_del("SSSSsssshhhh"))
    print(sequence_del("Heeyyy   yyouuuu!!!"))


if __name__ == "__main__":
    main()