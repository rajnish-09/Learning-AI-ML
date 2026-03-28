# Input string and check whether it is palindrome or not
txt = input("Enter a string: ")
txt1 = ''
reversed_text = txt[::-1]
if txt==reversed_text:
    print(f"{txt} is palindrome.")
else:
    print(f"{txt} is not palindrome")