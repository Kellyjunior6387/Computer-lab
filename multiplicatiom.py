#Function to print the table that takes the integer as input
def mutliplication_table(number):
    for i in range(1, 11):
        product = i * number
        print(f"{number} X {i} = {product}") 

number = int(input('Enter the number:'))

mutliplication_table(number)