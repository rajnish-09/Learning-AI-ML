# Write program to handle exception when divided by 0


try:
    x = int(input("Enter a number: "))
    ans = 10/x
except ZeroDivisionError:
    print("Cannot divide number by zero.")
else:
    print(f'After division: {ans}')
finally: 
    print("End of program!")


