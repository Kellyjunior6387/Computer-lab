def prime_number_checker(number, divisor = 2):
    if number <= 1:
        return False
    if divisor  * divisor > number:
        return True
    if number % divisor == 0:
        return False
    return prime_number_checker(number,divisor+1)

number = int(input("Enter the number:"))

prime_number = prime_number_checker(number)

if(prime_number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")