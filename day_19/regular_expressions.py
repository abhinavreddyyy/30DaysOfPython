import re
txt = 'I love to teach python and javascript'
match = re.search("I love to te", txt, re.I)
print(match)
span = match.span()  
print(span)

