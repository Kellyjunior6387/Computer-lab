def cube(number):
    result = number * number * number
    return result

number = int(input('Enter the number:'))
print(f"The cube of {number} is {cube(number)}")