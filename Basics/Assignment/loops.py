# Write a function that determines prime factors between i and n

def prime(n):
    for n in range(0,n):
        if(n % 1 == 0 and n % 2 != 0 and n % 5 != 0  and n % 3 != 0 ):
            print(n,'is a prime number')
prime(27)

