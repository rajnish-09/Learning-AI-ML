# Input string from user and list and count all unique characters

inp = input("Input: ")
seen = set()
duplicates = set()
for i in inp:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)
print(f"Unique characters {seen-duplicates}")
print(len(seen-duplicates))