# phone regex

import re

text = 'My phone number is +254-111-947-937'
pattern = r'[+]\d{3}-\d{3}-\d{3}'

match = re.search(pattern,text)

if match:
    phoneNumber = match.group()
    print('Phone number found',phoneNumber)
else:
    print('Phone number not found')

