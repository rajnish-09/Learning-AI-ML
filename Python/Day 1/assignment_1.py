# Q.1: Write a program to ask user for their name, age and print them
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
print("Hello "+name +", you are",age,"years old!\n")


# Q.2: Take two numbers input and print their sum, difference, product and quotient
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum:",(num1+num2))
print("Difference:",(num1-num2))
print("Product:",(num1*num2))
print("Quotient:",(num1%num2))


# Q.3: Ask the user to enter two integers and one float. Convert them all to floats and print their average
n1 = int(input("\nEnter first integer: "))
n2 = int(input("Enter second integer: "))
n3 = float(input("Enter third float:"))
n1 = float(n1)
n2 = float(n2)
average = (n1+n2+n3)/3
print(f"The average is {average}")


# Q.4: The user enters a string containing a number(e.g. 45).Convert it •an integer •a float •a string again .Print all three values with their types
number1 = input("Enter a number: ")
number1 = int(number1)
print(number1, type(number1))
number1 = float(number1)
print(number1, type(number1))
number1 = str(number1)
print(number1, type(number1))


#Q.5: Evaluate and print ->     x = 10+3*2**2
x = 10+3*2**2
print(x)


# Q.6: WAP to swap values of two numbers entered by user
val1 = int(input("Enter first value: "))
val2 = int(input("Enter second value: "))
temp = val2
val2 = val1
val1 = temp
print("Value 1: ",val1)
print("Value 2: ",val2)


# Q.7: Ask user for temperature in celsius (String input). Convert it to float, then calculate and print temperature in farenheit
celsius_temp = input("Enter temperature in celsisus:")
celsius_temp = float(celsius_temp)
farenheit_temp = (celsius_temp*(9/5))+32
print("After converting, Temp:",farenheit_temp)


# Q.8: Take the radius as user input and print the area
radius = float(input("Enter the radius: "))
area = 3.14*radius*radius
print("The area of circle is",area)

# Q.9: Ask for principal, rate and time. Convert all to float and compute simple intrest
p = float(input("Enter principal amount: "))
t = float(input("Enter time: "))
r = float(input("Enter rate: "))
si = (p*t*r)/100
print("The SI is",si)


# Q.10: Take a decimal number as input and output its -- integer part and fractional part
number = float(input("Enter a decimal number: "))
int_part = int(number)
fraction_part = number-int_part
print("Integer part:",int_part)
print("Fractional part:",fraction_part)