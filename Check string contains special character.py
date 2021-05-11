# Input : "Welcome@@2To%%Python**Programming@!!^%%@$"
# Output : String contains special character

#Input : "Welcome to python programming"
#Output: No special charcter in the string

import re

str = "Welcome@@2To%%Python**Programming@!!^%%@$"

regex = re.compile('[@_!#$%^**()/\|:!`~]')   #Regular Expression.

if(regex.search(str) == None):
    print("No special charcters present in the string")
else:
    print("String contains special charcters")