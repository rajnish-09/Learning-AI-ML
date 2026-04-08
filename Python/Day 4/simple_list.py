# Display list items
animals = ['cat', 'dog', 'elephant', 'leopard', 'lion']
print(animals)

# Append 5 numbers to empty list
numbers = []
for i in range(10):
    numbers.append(i+1)
print(numbers)

# Finding sum of the numbers in list
sum = 0
for i in range(len(numbers)):
    sum += numbers[i]
print(sum)

# Count the even numbers in the list
count = 0
for i in range(len(numbers)):
    if numbers[i]%2==0:
        count+=1
print(count)

# Find the maximum number from the list
max = 0
for i in range(len(numbers)):
    if numbers[i]>max:
        max = numbers[i]
print("Largest number:",max)

# Reverse the list
for i in range(len(numbers), 0, -1):
    print(numbers[i-1])
    
# Remove duplicate items from the list
num = [1,4,2,4,6,8,1,3,5,1]
unique_list = list(dict.fromkeys(num)) # Using dictionary. Dictionary doesn't allow duplicate values
print(unique_list)

# Check number if it exist or not in list
a = int(input("Enter a number to check: "))
print(a in num)     #True if exists, and False if it doesn't

