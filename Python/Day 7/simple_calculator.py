# Program to create simple calculator using function

def calculator(a,b,operator):
    if(operator == '+'):
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    elif operator == '/':
        return a/b
    elif operator == '**':
        return a**b
    elif operator == '%':
        return a%b
    else:
        return "Invalid operator" 
    
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+,-,*,/,**,%): ")
result = calculator(num1, num2, operator)
print(result)
