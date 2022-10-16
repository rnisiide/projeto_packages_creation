#Testing package
from Learn_math import operations

print("We will use this calculator to learn the basic math operations. Please choose two values:")
value1= float(input("First value: "))
value2= float(input("Second value: "))
operator = int(input("Select wich operation you would like to learn about. Type:\n [1] for sum: \n [2] for subtraction: \n [3] for multiplication: \n [4] for division: "))

if operator == 1:
    print(operations.sum(value1, value2))

elif operator == 2:
    print(operations.subtraction(value1, value2))

elif operator == 3:
    print(operations.multiplication(value1, value2))

elif operator == 4:
    if value2 == 0:
        print("Division by zero is impossible! Please start over") 
    else:
        print(operations.division(value1, value2))      
