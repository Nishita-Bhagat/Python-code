import re
str = "I am blogger at http://www.pawantestingtools.com/"
str1 = "My profile: https://www.pwanonlinetrainings.com/about.html"

# http://urlregex.com/
# http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+

url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',str1)

print(url)