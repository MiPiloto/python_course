import json

print("Let me guess your favorite number...")
filename = 'username.json'
with open(filename) as filename:
    number = json.load(filename)

print("Your number is " + str(number) + "!")