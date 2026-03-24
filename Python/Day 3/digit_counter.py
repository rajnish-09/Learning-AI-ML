# Q: WAP to count number of digit in a number
# /= performs floating-point division
# //= performs integer division

num = int(input("Enter a number: "))
count = 0
while(num>0):
    num //= 10
    count+=1
print(count)
