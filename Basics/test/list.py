list = ['1','Adam','Meran']
print(list)

# methods of lists
# list.append -add elements at the end of a list
# list.insert(element.index)  -inserts elements at the specified position of a list
# list.extend(list2) - adds a different list into the same index list
# List.remove(element) - removes element from the specified list
# list.index
# list.sort()

list1= ['apple','orange','banana','kiwi']

print(list1)

list2 =['apple',[3,4,5],'orange','banana']
print(list2)
# index
print(list1[2])
# list within a list
print(list2[1][2])
# reverse
print(list1[-1])
# slicing
print(list1[1:3])
# 
print(list1[3:])
# appending

list1.append('guava')

print(list1)
# extending

list1.extend(['watermelon','muskmelon'])

print(list1)
# deleting an array 

del list1[5]
print(list1)

# deleting an array
#  list1.remove('kiwi')
#  print(list1)
# pop

print(list1.pop(2))
# reverse

list1.reverse()
print(list1)
# indexing

print(list1.index('guava'))
