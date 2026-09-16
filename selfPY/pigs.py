num = int(input("Enter a number with three digits : "))

hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

total_bricks = hundreds + tens + units
bricks_per_pig = total_bricks // 3
remainder = total_bricks % 3
is_divisible = (remainder == 0)

print(total_bricks)
print(bricks_per_pig)
print(remainder)
print(is_divisible)

