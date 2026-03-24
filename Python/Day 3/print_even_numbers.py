# Q: Print all even numbers between numbers
# range (start_value? , stop_value, step?) -> ? means optional

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Even numbers are: ")
for i in range(num1,num2):
    if(i%2==0):
        print(i)