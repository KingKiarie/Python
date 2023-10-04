# Coding Challenge: Regular Expressions in Python
# Objective:
# To understand and implement regular expressions in Python to match and extract specific patterns from a given string.
# Instructions:
# Use the re module in Python to implement regular expressions
# Write a function called extract_phone_numbers(string) that takes in a string and returns a list of all the phone numbers present in the string in the format (XXX) XXX-XXXX
# Write a function called extract_email_addresses(string) that takes in a string and returns a list of all the email addresses present in the string.
# Write a function called replace_email_addresses(string, replacement) that takes in a string and a replacement string, and replaces all email addresses in the given string with the replacement string.
# Use the provided test cases to test your functions
# Example:
# string = "Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333" print(extract_phone_numbers(string)) # Output: ['(123) 456-7890', '(111) 222-3333'] print(extract_email_addresses(string)) # Output: ['info@example.com'] print(replace_email_addresses(string, "REPLACED")) # Output: "Please contact REPLACED for assistance. Phone: (123) 456-7890 or (111) 222-3333" 
# Note:
# Phone numbers and email addresses can appear in any order and more than once in the provided string.
# Phone numbers may or may not have spaces or dashes in between digits.
# Email addresses may or may not have .com, .edu, .gov, etc.
# Be mindful of edge cases
# Hint:
# Phone number regex pattern: "(?\d{3})?[-.\s]?\d{3}[-.\s]?\d{4}"
# Email address regex pattern: "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
# Submission:
# Create a python file named coding_challenge.py and paste your functions and test cases inside.
# string = "Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333"
# print(extract_phone_numbers(string))
# # Output: ['(123) 456-7890', '(111) 222-3333']
# print(extract_email_addresses(string))
# # Output: ['info@example.com']
# print(replace_email_addresses(string, "REPLACED"))
# # Output: "Please contact REPLACED for assistance. Phone: (123) 456-7890 or (111) 222-3333"
# reeference to guide.py under regex/guide/guide.py

# import re

# def extract_phone_numbers(string):
#     phone_pattern = r'\(?\d{3}\))?[-.\s]?\d{4}'


# def extract_email_address(string):


# def replace_email_address(string):



