import re

def match_pattern(pattern,text):
    match = re.search(pattern, text)
    if match:
        print('pattern found')
    else:
        print('Pattern not found')
match_pattern('Have','I have an apple and a banana')


# write a function that takes in two parameters pattern and text. If the text matches the pattern print out the keyword that matched the pattern

import re

def match_words(pattern,text):
    match = re.search(pattern,text)

    if match:
        print('pattern found',match)
    else:
        print('pattern not found')

match_words('cream','I deam to be soft as cream , lovely as the tides go i might scream my whip, to savor the flavor i will wipe my cream')