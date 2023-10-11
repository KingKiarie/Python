names= ['Joe','doe','foe']

for name in names:
    print('Hello ',name)
    

# Largest so far
# largest_so_far =-1
# count = 0

# for num in [22,33,45,6,7,789,90,5]:
#     print(num)
#     largest_so_far = num
#     print(largest_so_far)
#     count = count + 1

# print(count ,largest_so_far )


name = 'KevinKiarie'
index = 0


while index < len(name):
    letter = name[index]
    index = index +1
    print(index,letter)


fruit = 'thornMelon'

frame = 1

while frame < len(fruit):
    sl = fruit[frame]
    frame = frame+1
    print(frame,sl)


print(fruit[:4])