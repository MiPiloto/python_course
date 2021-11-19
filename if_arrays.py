# welcome 

users = ["admin","tony","clark","peter","bruce"]

if users:
    for user in users:
        if user == "admin": print("Welcome back, master!")
        else: print("Hello " + user.title() + ", welcome!")
else: print("No one here!\n")

# new users

current_users = users[:]
new_users = ["tony","peter","widow","strange","hank"]

for new_user in new_users:
    if new_user.lower() in current_users: print("User already registered, choose a new username!")
    else: print("Welcome, " + new_user.title() + "!")

# ordinal numbers

ordinals = [1,2,3,4,5,6,7,8,9]

for ordinal in ordinals:
    if ordinal == 1: print(str(ordinal) + "st!")
    elif ordinal == 2: print(str(ordinal) + "nd!")
    elif ordinal == 3: print(str(ordinal) + "rd!")
    else: print(str(ordinal) + "th!")


