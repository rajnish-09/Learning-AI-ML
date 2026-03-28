# From list, list out all the elements that repeat more than once

list1 = [1,2,3,4,5,4,3,7,6,7,9]
seen = set()
duplicates = set()

for i in list1:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)
print(f"Duplicates: {duplicates}")