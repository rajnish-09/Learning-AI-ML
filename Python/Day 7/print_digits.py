# Program to print its digit using function

def print_digits(a):
    digits = ''
    while(a>0):
        digit = a%10
        a //= 10
        digits = digits + str(digit)
    return digits[::-1]

print(print_digits(123))

