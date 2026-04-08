# Creating set
set1 = {1,2,3,4}
print(type(set1), set1)
set2 = set((1,2,3,4,4))
print(type(set2), set2)


# Looping in set
for i in set1:
    print(i)


# Removing item
set1.remove(2)
print(set1)

set1.discard(40)
print(set1)


# Different set operations
a = {1,2,5,3,6}
b = {2,5,0,8,7}

# Union (|)
c = a.union(b)
print(c)
d = a | b
print(d)

# Intersection (&)
e = a.intersection(b)
print(e)
f = a & b
print(f)

#Difference(-)
g = a.difference(b)
print(g)
h = a - b
print(h)




