class person:
    def __init__(self,name, age, occupation):
        self.name = name
        name = input()
        self.age = age
        self.occupation = occupation
    def greet(self):
        print('hello' , self.name)
    def cry(self):
        print(f'{self.name}, is a crybaby')

myPerson = person('Kevin',22,'Software Dev')

print(myPerson.name)
print(myPerson.age)
print(myPerson.occupation)
myPerson.greet()
myPerson.cry()



