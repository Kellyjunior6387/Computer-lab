
def factorial(number):
    if number < 0:
        raise ValueError("Number must be a positive integer")   
    if number == 0:
        return 1
    return number * factorial(number - 1)

number = int(input('Enter the number:'))
try:
    print(f"{number}! = {factorial(number)}")
except:
    print("Something went wrong")