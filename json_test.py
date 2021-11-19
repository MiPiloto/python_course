import json


filename = 'username.json'
print("Let me guess your favorite number...")

try:
    with open(filename) as filename:
        number = json.load(filename)

    
except FileNotFoundError: 
    fav_number = input("What's your favorite number? ")
    with open(filename,'w') as filename:
        json.dump(fav_number,filename)
    print("Saved your number!")
else:
    print("Your number is " + str(number) + "!")



