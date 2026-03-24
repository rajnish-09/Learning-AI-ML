# WAP to find palindrome number

num = int(input("Enter a number: "))
reverse = 0
temp = num
while(num>0):
    digit = num%10
    reverse = reverse * 10 + digit
    num //= 10
if(reverse == temp):
    print(f"{temp} is palindrome number")
else:
    print(f"{temp} is not palindrome number")