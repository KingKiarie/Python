# lines =[1,2,3,4,5,6,7,8,9]

# with open('text.txt','r')as textfile:
#     textfile.writelines(lines)

# Write a python program that reads the words.txt file and prints out all the palindromes in the file to a palindromes.txt file

# reading a file
file = open('words.txt', 'r' )
content = file.read()

# print(content)

# palindrome checker functions

def is_palindrome():
    string = input('Enter your words:')

    if string == string [::-1]:
        print(string,'is a palindrome')
    else:
        print(string, 'is not  palindrome')

# is_palindrome()

# program that checks if words in a file are palindromes
# attempt 1
# def find_palindrome():
#     with open('words.txt','r')as f:
#         for x in f:
#             line = x.strip()
#             if line == line[::-1]:
#                 with open('palindrome.txt','r+')as f2:
#                     f2= f2.writelines(line)
#                     print(f2)
                        
                            
# find_palindrome()

# attempt2

def find_palindome(fileA, fileB):
    with open('words.txt','r') as fileA:
        file = fileA.read()
        x = file.split()
        palindrome = [line for line in x if line == line[::-1]]
    
    with open('palindrome.txt','w') as fileB:
        for like in palindrome:
                fileB.writelines(like + '\n')

fileA = 'words.txt'
fileB = 'palindrome.txt'

find_palindome(fileA, fileB)