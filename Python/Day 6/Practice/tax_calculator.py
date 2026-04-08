# Take salary as input from user and calculate tax (<30000 -5%, 30000-70000 -15%, >770000 -25%)
salary = float(input("Enter your salary: "))
tax = 0
if(salary < 30000):
    tax = salary*0.05
elif(salary >= 30000 and salary <70000):
    tax = salary * 0.15
elif(salary >=70000):
    tax = salary * 0.25
else:
    print("Invalid salary")
print(f"Tax: {tax}")
    
