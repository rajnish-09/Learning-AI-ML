# From the given tuple, create tuple of even and odd numbers
tup = (1,2,3,4,5,6,7,8,9,10)
even_tuple = ()
odd_tuple = ()
for i in tup:
    if i%2==0:
        even_tuple += (i,) 
    else:
        odd_tuple += (i,)

print(even_tuple)
print(odd_tuple)
