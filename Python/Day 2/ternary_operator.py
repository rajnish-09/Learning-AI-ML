# There are two ternary operator (single line if and clever if)
# Using single line if -> For this example only use animal name cat or dog to show animal
animal = input("Enter a animal name: ")
result = 'Animal' if animal == 'cat' or animal == 'dog' else 'Not animal'
print(result)


# Using clever if 
print("\nVoting eligibility test")
age = int(input("Enter your age: "))
res = ('No', 'Yes') [age>=18]       # ("False_value", "True_value")
print(res)