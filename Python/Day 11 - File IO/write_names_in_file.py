# Create a file name names.txt in write mode. Write 5 names (one name at a line) entered by the user. Then open the same file in read mode and display all names

i = 1
with open("names.txt", 'w') as f:
    while i<=5:
        name = input("Enter a name: ")
        f.write(name + "\n")
        i += 1

with open("names.txt", 'r') as f:
    print(f.read())