# Write a program that tires to open data.txt file in read mode. If the file does not exist, catch the exception and print File not found

try:
    with open("data.txt", 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
finally: 
    print("End of program")

