# Challenge: Vowel Counter
# Write a function called count_vowels that takes a string as input and returns the count of vowels (a, e, i, o, u) in the given string. The function should be case-insensitive, meaning it should count both uppercase and lowercase vowels.
# Example:
# python

# count_vowels("Hello, World!") # Output: 3 
# count_vowels("Python is awesome!") # Output: 6 
# count_vowels("AEIOU") # Output: 5 
# Note:
# You can assume that the input string will only contain alphabetic characters.
# Spaces and special characters should not be counted as vow

def count_vowels(string):

    count = 0

    for character in string:
        if(character in string):
            count += 1

    return count

string= input('string:')
count= count_vowels (string)

print('Count:', count)