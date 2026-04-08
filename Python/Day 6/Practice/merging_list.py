# Enter two list of integer from user and merge them
list1 = list(map(int, input("Enter first list items: ").split()))
list2 = list(map(int, input("Enter second list items: ").split()))
list3 = list1 + list2
print(f"After merging: {list3}")