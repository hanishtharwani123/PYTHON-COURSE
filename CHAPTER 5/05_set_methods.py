# creating an empty set 
b = set()
print(type(b))


# adding values to an empty set
b.add(4)
b.add(5)
b.add(5)
 
# set is collection of non repetitive elements
print(b)

# list and dictionary will not add in empty set but tupple will add

print(len(b))

b.remove(5)
print(b)

print(b.pop())