# alien color if elif else program

alien_color = "green"
alien2_color = "yellow"
alien3_color = "red"

if alien_color == "green": print("You gained 5 point!")
if alien_color == "yellow": print("You gained 10 points!")

if alien2_color == "green": print("5 points!")
elif alien2_color == "yellow": print("10 points!")
else: print("15 points!")

# Life Cicle Program

age = 33

if age < 2: print("You're a baby!")
elif age >= 2 and age < 4: print("You're a child!")
elif age >=4 and age < 13: print("You're a teen!")
elif age >=13 and age < 20: print("You're a juvenile")
elif age >= 20 and age < 65: print("You're an adult!")
else: print("You're old!")

# Favorite Fruit

fav_fruit = ["apple","banana","peach","strawberry","melon"]

if "banana" in fav_fruit: print("You really like bananas!")
if "watermelon" in fav_fruit: print("Watermelons are good!")
else: print("No watermelons today!")