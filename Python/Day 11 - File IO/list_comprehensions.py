# Create a list of numbers and use list comprehension to create new list with numbers greater than 15 and print them

nums = [ 2,5,20,14,36,75,44]

greater_than_15 = [i for i in nums if i>15]
print(greater_than_15)