# Creating tuple
tuple1 = (1,2,3,4,2,5,1,3,2)
print(type(tuple1), tuple1)

# Accessing tuple element
print(tuple1[3])    # Prints 4

# Unpacking tuple
(a,b,*c) = tuple1
print("a:",a)
print(c)

# Tuple methods
print(tuple1.count(1))  # Count number of occurance of 1
print(tuple1.index(1))  # Print first occurance index of element 1