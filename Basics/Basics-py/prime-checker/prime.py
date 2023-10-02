while True:
    print('Hello world')
    break

# Print a for loop that prints numbers between 1-100

# for i in range(0,100):
#     print(i + 1)

# even numbers

for num in range(0,100):
    if(num % 2 == 0):
        print(num,'is even')

# write a python program that prints odd numbers from 0 -20

for num in range(1,100):
    if(num % 1 == 0 and num % 3 == 0 ):
        print(num, 'is odd')

        # write a python program that prints all the multiples of 7 between 0-1000

# for num in range (0,1000,7):
#     print(num,'Is a multiple of seven')


def even_Numbers(n):
    for i in range(50,n):
        if(i % 2 == 0 ):
            print(n, 'ís an even number')
even_Numbers(200)