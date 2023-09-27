# Write a python program that reads the words.txt file and prints out all the palindromes in the file to a palindromes.txt file

#basic reading a file 
file = open('words.txt', 'r' )
content = file.read()

 print(content)# reads the file

#basic palindrome checker function

def is_palindrome():
    string = input('Enter your words:')

    if string == string [::-1]:#this is a reverse function to tell if the word while inverted is the same
        print(string,'is a palindrome')
    else:
        print(string, 'is not  palindrome')

 is_palindrome()

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
# this function has two parameters where fileA is where we read the data and fileB is the output to the palindrome words
def find_palindome(fileA, fileB):
    with open('words.txt','r') as fileA:
        file = fileA.read()
       #.split() divides the words into single letters 
        x = file.split()
        #create a palindrome array where it will check for every letter in each word that has been split check if its reverse is equal to it while inverted
        palindrome = [line for line in x if line == line[::-1]]
    
    with open('palindrome.txt','w') as fileB:
        for like in palindrome:
                fileB.writelines(like + '\n')

fileA = 'words.txt'
fileB = 'palindrome.txt'

find_palindome(fileA, fileB)