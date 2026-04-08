# Creating dictionary
student = {
    "name":"Rajnish",
    "roll":1,
    'age':20
}
print(type(student), student)

# Accessing the dictionary
print(student.get("name"))  # Prints name value
print(student['roll'])      # Prints roll value

# Adding or modifying values
student['name'] = 'Rakesh'
print(student["name"])      # Prints updated value (Rakesh)


# Looping through dictionaries
for key in student:
    print(key, student[key])

for k, v in student.items():
    print(k, v)

# Removing element
student.pop("roll") # Removes key-value pair
print(student)      
student.popitem()   # Removes the last key-value pair
print(student)
student.clear()     # Clears the dictionary
print(student)  

