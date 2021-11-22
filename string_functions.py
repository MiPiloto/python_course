# f strings
x = 7
s = f'This number is now a string {x:d}'
print(s)
# creating blank space to show integer position
s1 = f'[{27:10d}]'
print(s1)
# creating blank space to show float position, default with six digits
s2 = f'[{2.7:10f}]'
print(s2)
# positioning with f strings
# left align
s3 = f'[{2.7:<15f}]'
print(s3)
# right align
s4 = f'[{2.7:>15f}]'
print(s4)
# center align
s5 = f'[{2.7:^15f}]'
print(s5)
# adding thousand separators ","
s6 = f'{345899876:,d}'
print(s6)

# concatenating and repeating
a = "hello"
b = "world"

a += ' ' + b
print(a)
b *= 5
print(b)

# removing whitespace
c = "  white space test  "
# strip removes all white spaces
c1 = c.strip()
print(c1)
# lstrip removes left white spaces
c2 = c.lstrip()
print(c2)
# rstrip removes right white spaces
c3 = c.rstrip()
print(c3)

# change letter case
# capitalize changes the first letter uppercase
c4 = c.capitalize()
print(c4)
# title changes the first letter of every word to uppercase
c5 = c.title()
print(c5)
# upper makes all string uppercase
c6 = c.upper()
print(c6)
# lower makes all string lower
cc = "  Hello WORLD  "
c7 = cc.lower()
print(c7)

# operations with substrings
# searching for substrings
d = "this string is a test, and a test is this string"
# count the substrings passed as args in the string
d1 = d.count("string")
print(d1)
# first position of the word in the string
d2 = d.index("string")
print(d2)
# last position of the word in the string
d3 = d.rindex("string")
print(d3)
# checking if a string contains a substring
print("string" in d)
print("this" not in d)
# locating substrings in the beginning or in the end of the string
d4 = d.startswith("this")
print(d4)
d5 = d.endswith("test")
print(d5)
# replacing substrings, first arg is the substring to be substituted for the sencond arg
d6 = d.replace("string", "sentence")
print(d6)

# split and join
e = "tes,ting splitt,ing senten,ces"
# split with no args split the string in the withe spaces
e1 = e.split()
print(e1)
# split can be used with args for markers to split
e2 = e.split(",")
print(e2)
# joining strings with separator " " and ","
f = ["testing joining", "strings", "in a single one"]

f1 = " ".join(f)
print(f1)
f2 = ",".join(f)
print(f2)

# character testing
# isdigit returns true if the string contains only 0-9 chacaracters
# returns false
g = "-45"
g1 = g.isdigit() 
print(g1)
# returns true
h = "45"
h1 = h.isdigit()
print(h1) 
# isalnum returns true if all characters are alphanumeric
# returns true
i = "123abtPoKjd"
i1 = i.isalnum()
print(i1)
# returns false
j = "123 abt PoK jd"
j1 = j.isalnum()
print(j1)
# other functions that work the same way:
# isalpha returns true if all characters are alphabetic
# islower returns true if all characters are lowercase
# isupper returns true if all characters are uppercase
# istittle returns true if characters are formated in tittle format
# isspace returns true if the string has only white spaces
 
# raw strings
# file and file1 are equal. File1 uses raw string notation
file = "C:\\MyFolder\\MySubfolder\\MyFile.txt" 
file1 = r"C:\MyFolder\MySubfolder\MyFile.txt"
print(file)
print(file1)

# re functions

