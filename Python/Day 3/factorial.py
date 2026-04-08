# Q: Find factorial of input number

num = int(input("Enter a number: "))
i = 1
fact = 1
if(num==0):
    print("Factorial of 0 doesn't exist.")
elif num==1:
    print("Factorial of 1 is 1")
else:
    while(i<=num):
        fact *= i
        i+=1
    print(f"Factorial of {num} is {fact}")