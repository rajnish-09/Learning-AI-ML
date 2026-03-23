# Using nested condition to find largest number among three numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if(num1>num2):
    if(num2>num3):
        print(num1,"is greatest.")
    else:
        print(num3,'is greatest.')
if(num2>num1):
    if(num1>num3):
        print(num2,'is greatest.')
    