string = input("Please enter a string : ")

mid = len(string) // 2
first_half = string[:mid].lower()
second_half = string[mid:].upper()
result = first_half + second_half

print(result)