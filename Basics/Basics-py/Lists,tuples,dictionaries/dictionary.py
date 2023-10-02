# dictionaries are mutable
# methods used are:
# dict.clear() - removes elements in the  []
# dict.get([keyname]) - aqcuires value of the specified key
# dict.key() - returns a list containing dictionaries keys
# dict.pop(keyname) - removes element of the specified key
# dict.popItem() - removes item of the last possible key item


dict1 = {1:'apple',2:'john',3:'Fola',4:'Sinclaire'}


print(dict1)
print(dict1[2])
# acquires an element in the list based in the specified index
print(dict1.get(3))
# pop removes elements from the specific index
print(dict1.pop(4))
print(dict1)
# prints the number if elements in the array
print(len(dict1))
# sorts all the key values in the array
print(sorted(dict1))
# keys
print(dict1.keys())
# values
print(dict1.values())
# updating any element in the dict
dict1.update({2:'Watermelon'})
print(dict1)
# appending
dict1.update({4:'Conlar'})
print(dict1)
# removing the last element from the dictionary
dict1.popitem()
print(dict1)
# Loops in dictionaries

for name in dict1:
    print(dict1[name])
# gives the arrayed list an index and the info
for x,y in dict1.items():
    print(x,y)
# copying information in the dictionary onto another dictionary

dict_c = dict1.copy()

print(dict_c)


