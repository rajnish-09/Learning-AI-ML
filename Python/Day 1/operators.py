'''
Operators
1. Arithmetic 
2. Relational/Comparison
3. Assignment
4. Logical
'''

a = 9
b = 5

# --------------------------------
# Arithmetic operator (+,-,*,/,%, **)
# --------------------------------
print(a+b)      #14
print(a-b)      #4
print(a*b)      #45
print(a/b)      #1.8
print(a%b)      #4
print(a**b)     #59049 (calculates a^b)


# --------------------------------
# Relational operator (>, >= , <, <=, ==, != )
# --------------------------------
print(a>b)      #ture
print(a>=b)     #true
print(a<b)      #false
print(a<=b)     #false
print(a==b)     #false
print(a!=b)     #ture


# --------------------------------
# Assignment operator (=, +=, -=, *=, /=, %=)
# --------------------------------
c = 10
print(c)        #10
c += 3
print(c)        #13
c %= 3
print(c)        #1


# --------------------------------
# Logical operator (not, and, or)
# --------------------------------
var = True
print(not var)      #False
print(not (a>b))    #False
print((8>4) and (9>1))  #True
print((8>4) or (9<1))  #True

