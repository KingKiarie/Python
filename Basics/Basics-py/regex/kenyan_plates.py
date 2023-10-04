# write a regular expression pattern for a kenyan car number plate

# \w - matches any word character
# \s - matches any whitespace character
import re

def match_plate(pattern,alphanumeric):

    match = re.match(pattern,alphanumeric)

CarA = 'KCC 735 K'
pattern = r'\w{3}{s}\d{3}\w'

match_plate(pattern,CarA)