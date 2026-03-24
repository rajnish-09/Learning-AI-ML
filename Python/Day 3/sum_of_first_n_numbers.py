# Q: Find sum of first n natural numbers

num = int(input("Enter nth number: "))
i = 1
total = 0
while i<=num:
    total += i
    i+=1
print("Sum:",total) 