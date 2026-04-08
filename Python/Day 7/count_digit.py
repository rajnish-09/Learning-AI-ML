# Python program to print the count of digit using function

def count_digit(a):
    count = 0
    while(a>0):
        count +=1
        a //= 10
    return count

number = int(input("Enter a number: "))
print(f"The number {number} contains {count_digit(number)} digits")