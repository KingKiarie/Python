# Write a Python function is_palindrome(input_str) that takes a string as input and returns True if the string is a palindrome, and False otherwise.
# A palindrome is a word, phrase, or sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.]


def is_palindrome(input_str):
    if(input_str == input_str[::-1]):
        print(input_str,'is a palindrome Good Job!')
    else:
        print(input_str,'is not a palindrome try again.')


is_palindrome('nonc')