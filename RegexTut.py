import re as r

"""
Regex identifiers
\d any number
\D anything but a number
\s space
\S anything but a space
\w any character
\W anthing but a character
. is a character except a new line
\. is a period
\b is white space around words
"""

"""
Regex modifiers
{1, 3} we are expecting 1-3
+ Match 1 or more
? Match 0 or 1
* Match 0 or more
$ Match the end of the string
^ Matching the beginning of the string
| either or
[] range or variance
{x} expecting x amount of bits of data

White space character:
\n new line
\s space
\t tab
\e escape
\f form feed
\r  return 

Dont forget:
. + * [ ] ? $ ^ ( ) { } | \
"""

exampleString = """

Rehan is 26 years old , 
Pritesh is 24 years old, 
Akash is 23 years old, 
Santosh is 25 years old.

"""

# finding ages
ages = r.findall(r'\d{1,3}', exampleString)
print(ages)
names = r.findall(r'[A-Z][a-z]*', exampleString)
print(names)

exampleDict = {}

x = 0
for name in names:
    exampleDict[name] = ages[x]
    x += 1

print(exampleDict)
