# Take string as input and print number of spaces in the string
user_input = input("Enter something: ")
count = 0
for ch in user_input:
    if ch == " ":
        count +=1
print(count)