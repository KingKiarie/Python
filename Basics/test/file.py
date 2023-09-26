def is_palindrome(file1,file2):
    with open('file.txt','r')as Main:
        text = Main.read()
        sep = text.split()

        palindrome = [line for line in sep if line != line [::-1] ]
    with open('test.txt','w') as other:
        for like in palindrome:
            other.writelines(like+'\n')

file1 = 'file.txt'
file2 = 'test.txt'

is_palindrome(file1,file2)