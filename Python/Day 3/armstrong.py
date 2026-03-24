# WAP to find number is armstrong or not

num = int(input("Enter a number: "))
temp1 = temp2 = num
count = 0
total = 0
while(temp1>0):
    temp1 //= 10
    count += 1
while(temp2>0):
    digit = temp2%10
    temp2 //= 10
    total += digit**count
if total == num:
    print(f"{num} is armstrong number")
else:
    print(f"{num} is not armstrong number")