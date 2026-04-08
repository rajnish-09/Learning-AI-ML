# Create a dictionary to store name and marks of student
dict = {}
while(True):
    print('\nA: To add student \nB: To update marks \nC: To search student \nD: Display student and marks \nX: To exit')
    user_input = input("Enter from above: ")
    
    if user_input == "A":
        n = input("Enter student name: ")
        if n in dict:
            print("Student already exists.")
        else:
            dict.update({n: list()})
    elif user_input == 'B':
        n = input("Enter student name: ")
        if n in dict:
            marks = list(map(int, input("Enter student marks: ").split()))
            dict[n] = marks
        else:
            print("Student doesn't exist")
    elif user_input == 'C':
        n = input("Enter student name: ")
        if n in dict:
            print(f"Marks: {dict[n]}")
        else:
            print("Student not found")
    elif user_input == 'D':
        print(dict)
    elif user_input == "X":
        break
    else:
        print("Invalid")



    