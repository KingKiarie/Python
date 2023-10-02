def greet():
    print('hello Kevin')


greet()
# write a function full name that prints out the full name of an individual

name=input('Enter your name:')

def fullname():
    print(name)

fullname()


# write a function that takes in Age of a person and prints a statement about their age

def bio(name,age):
    print('Hey,'+name+' you are ' ,age ,' years old. Bye champ!')

bio('kevin',22)

def Bios(name,age):
    if(age>=18):
        print('Wonderful', name ,'Looks like you are eligible to vote'  )
    elif(age< 10):
        print(name,'You can swim only in the shallow end')
    else:
        print('you are not eligible to vote try again when you are 18',name)

Bios('Kevin Mbugua Kiarie',17)

def products(num1,num2):
    print(num1*num2)

products(2,4)