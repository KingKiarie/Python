import re

def extract_phone_numbers(string):
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(phone_pattern, string)

def extract_email_address(string):
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(email_pattern, string)

def replace_email_address(string, replacement):
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    with open('rep.csv', 'w') as chain:
        return re.sub(email_pattern, replacement, string)

string = input("Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333")
print(extract_phone_numbers(string))  
print(extract_email_address(string))  
print(replace_email_address(string, "Changed"))  
