# tuples are immutable meaning they cannot be changed
# can be accessed by index
# are ordered
# can accomodate different values

# methods
# indexing
# slicing
# concantenation
# repitition
# count

tup1 = ('apple','orange','banana','kiwi')
print(tup1)
tup2 =('apple')
# checks the type of value embedded as a string
print(type(tup2))

print(tup1[-1])
# slicing tuples from a given array of index
print(tup1[1:3])
# concantenation of strings
print((1,2,3,4)+(1,2,3,4))

# list
y = list(tup1)
y.append('guava')

tuple = tuple(y)
print(tuple)