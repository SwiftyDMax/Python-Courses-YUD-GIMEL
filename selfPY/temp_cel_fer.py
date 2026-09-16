temprature = input("Insert the temperature you would like to convert: ")

unit = temprature[-1].upper() # Can be C - Celsius or F - Fahrenheit
value = float(temprature[:-1])

if unit == 'C':
    converted = (value * 9/5) + 32
    print(f"{int(converted) if converted.is_integer() else converted}F")
elif unit == 'F':
    converted = (value - 32) * 5/9
    print(f"{int(converted) if converted.is_integer() else converted}C")
else :
    print("INVALID INPUT")


