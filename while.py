pizza_ing = ""
prompt = "What ingredients do you want to add to your pizza? "
while pizza_ing != "quit":
    pizza_ing = input(prompt)
    if pizza_ing != "quit": 
        print(pizza_ing.title() + " will be added to the pizza!")

age = 0
active = True
while active:
    age = input("How old are you? Type 0 to quit. ")
    age = int(age)
    if age == 0:
        active = False
    if age > 3 and age <= 10:
         print("Your ticket costs 3 dolars.")
    elif age > 10 and age <= 14:
        print("Your ticket costs 14 dolars.")
    elif age > 14 and age <= 60:
        print("Your ticket costs 60 dolars.")
    else:
        print("You are too old or too young to go to the movies hahaha!")
    
    
