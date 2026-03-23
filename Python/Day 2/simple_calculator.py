num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (+,-,*,/,%,**): ")
if(operator == '+'):
    print("Sum:",(num1+num2))
elif(operator == '-'):
    print("Difference:",(num1-num2))
elif(operator == '*'):
    print("Multiplication:",(num1*num2))
elif(operator == '/'):
    print("Division:",(num1/num2))
elif(operator == '%'):
    print("Quotient:",(num1%num2))
elif(operator == '**'):
    print(num1,"to the power",num2,"is",(num1**num2))
else:
    print("Invalid operator!")