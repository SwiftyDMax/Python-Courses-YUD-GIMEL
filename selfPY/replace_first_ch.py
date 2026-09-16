string_input = input("Please enter a string: ")

first_char = string_input[0]
rest_of_str = string_input[1:]
new_string = rest_of_str.replace(first_char, 'e')

print(first_char + new_string)