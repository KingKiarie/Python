# ^ - matches beginning of a line
#  $ - matches the end of the line
# .\w - matches any character
#  \s - matches whitespace
# \s - matches any non-whitespace character
# *- repeats a character zero or more times
#  *? - repeats a character zero or more times(non-greedy)
#  + - repeats a character one or more times
#  +? - repeats a character one or more times (non-greedy)
# [aeiou] - Matches a single character in the listed set
# [^XYZ] - Matches a singl character not in the Listed set
# [a-z0-9] - The set of characters can include a range
# { - indicates where a string  extraction is to start
# } - indicates where string extraction is to last

# regular expression  = regex

# hand = open('guide.txt')

# for finger in hand :
#     finger = finger.rstrip()
#     if finger.find('men')>=0:
#         print(finger)

# import re

# gender= open('guide.txt')
# for man in gender:
#     man = man.rstrip()
#     if re.search('men',man):
#         print(man)


import re

gender = open('guide.txt')

for man in gender:
    man = man.rstrip()

    if re.search('sight',man):

        print(man)

import re 

xl= 'in the inn i found rest. in the inn away from the rest. in the in i tried to dread. in the in i come in test'
x = "2 of my mates are lovely, only time can decipher the 3 in space. I for 1 can atone greatness,for my love is only in 1's and 0's"
y = re.findall('[0-9]+',x)
y = re.findall('[Aeiou]+',x)

print(y)