import re
# importing re module

# fullmatch 
x = "I am an example"
y = "I am another example"
# fullmatch compares if two objects are exactly the same
print("It's a Match!" if re.fullmatch(x, "I am an example") else "No Match!")
print("It's a Match!" if re.fullmatch(x, y) else "No Match!")
# metacharacters, character classes and quantifiers
# \d checks for a digit 0-9, and {7} makes it 7 times
# \d{7} is equal to \d\d\d\d\d\d\d
print("True" if re.fullmatch(r'\d{7}', '1234567') else "False")
# \d checks for digits. \D checks for no digits
print('Valid' if re.fullmatch(r'\D{2}', "ab") else "Invalid")
# \s checks for whitespace \S checks for no whitespace
print('White!' if re.fullmatch(r'\s{3}', "   ") else "Black!")
print('White!' if re.fullmatch(r'\D{5}', "hey ya") else 'Black!')
# \w checks for alphanumeric, that is letters, digits or underscores \W checks for no alphanumeric
print('Alpha!' if re.fullmatch(r'\w{7}', 'hello_w') else 'false')
print('Alpha!' if re.fullmatch(r'W{3}', 'hey') else 'false')

# classes
# [aeiou] matches one vowel
# [A-Z] matches one uppercase letter
# [a-z] matches one lowercase letter
# the symbol ' * ' is a quantifier that matches zero or more of that class
print("Match!" if re.fullmatch('[A-Z][a-z]*', 'Hello') else "No Match")
# the symbol ' + ' is a quantifier that matches at lest one or more of that class
print('Match!' if re.fullmatch('[A-Z]+[a-z]*', 'hello') else 'False')
# the symbol ' ? ' is a quantifier that matches zero or one of a subexpression
print('Match!' if re.fullmatch('Arth?ur', 'Arthur') else 'False')
print('Match!' if re.fullmatch('Arth?ur', 'Artur') else 'False')
print('Match!' if re.fullmatch('Arth?ur', 'Arthhur') else 'False')
# the symbol ' {n,} ' is a quantifier that matches at least 'n' numbers of the expression
print('Digits!' if re.fullmatch(r'\d{5,}', '1234567') else 'False')
# the symbol ' {n,m} ' is a quantifier that matches 'n' and 'm' (inclusive)
print('Digits!' if re.fullmatch(r'\d{2,5}', '1234') else 'False')

# replacing substrings and splitting strings
# function sub replaces all occurrences of a pattern with the element specified
print(re.sub('\t', ',', '1\t2\t3\t4'))
print(re.sub('s', 'z', 'this is a sssnake string!'))
# function split
# example splitting a string at a comma followed by 0 or more whitespace characters
print(re.split(r',\s*', 'this, is,   an, example   of,  a     long    string'))

# search functions
# search returns the first occurrence of a substring
example = 'Coding is fun, and all we want is to have fun'
result = re.search('fun', example)
print(result.group() if result else 'Not found')
# flags oprional argument change the bahavior of search
# IGNORECASE searches for uppercase or lowercase
result2 = re.search('coding', example, flags=re.IGNORECASE)
print(result2.group() if result2 else 'Not found')
# metacharacter '^' searches the start of the string
result21 = re.search('^Coding', example)
print(result21.group() if result21 else 'Not found')
# and $ searches the end of the string
result22 = re.search('fun$', example)
print(result22.group() if result22 else 'Not found')
# match searches only at the beginning of the string
result3 = re.match('Coding', example)
print(result3.group() if result3 else 'Not found')
result4 = re.match('fun', example)
print(result4.group() if result4 else 'Not found')
# findall finds all matches of a substring and returns a list
# extracting all 3 or more digit numbers from a string
example2 = 'This 123 example has 45 numbers 6789 mixed in it 02468'
result5 = re.findall(r'\d{3,}', example2)
print(result5)
# finditer works like findall but returns one match at a time, saving memory in large searches
# finditer must be used as an iterable
for result6 in re.finditer(r'\d{3,}', example2):
    print(result6.group())

# substrings can be captured in a match
example3 = 'Bruce Wayne, e-mail: batman@batcave.com'
example4 = 'Darth Vader, e-mail: darkside@oftheforce.com'
# [A-Z][a-z]+ [A-Z][a-z]+ searches for two words starting with an uppercase letter
# \w+@\w+\.\w{3} searches for one or more alphanumeric, the @ character, one or more alphanumeric,
# a dot, and three alphanumeric characters
pattern = r'([A-Z][a-z]+ [A-Z][a-z]+), e-mail: (\w+@\w+\.\w{3})'
result7 = re.search(pattern, example3)
result8 = re.search(pattern, example4)
# group returns the entire match as a single string
print(result7.group())
print(result7.groups())
# groups returns the match as a tuple
print(result8.group())
print(result8.groups())

