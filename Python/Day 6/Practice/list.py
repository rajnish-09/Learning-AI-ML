# Check if two list have same elements or not

list1 = list(map(int, input("Enter elemts of first list: ").split()))
list2 = list(map(int, input("Enter elemts of second list: ").split()))
if set(list1) & set(list2):
    print("Contains common element")
else:
    print("Does not contain common element")