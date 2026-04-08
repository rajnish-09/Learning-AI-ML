# Open a file named logs.txt in append mode and add Program run successfully. Open the file in read mode and print all the logs

with open("logs.txt", 'a') as f:
    f.write("Program run successfully.")

with open("logs.txt", 'r') as f:
    data = f.read()
    print(data)