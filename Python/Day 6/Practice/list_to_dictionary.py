# From the list create dictionary that maps words with its length
fruits = ['apple', 'mango', 'banana', 'strawberry', 'kiwi']
fruit_dictionary = {}
for fruit in fruits:
    length = len(fruit)
    fruit_dictionary.update({fruit: length})
print(fruit_dictionary)
