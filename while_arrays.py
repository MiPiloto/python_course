sandwich_orders = ["x-tudo","americano","beirute","acebolado","pastrami","pastrami","pastrami"]
finished_sandwiches = []

print("Make your order:\nWe are out of pastrami today!")
while "pastrami" in sandwich_orders: sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwiche = sandwich_orders.pop()
    print("Your " + sandwiche.title() + " is ready!")
    finished_sandwiches.append(sandwiche)

for sandwiches in finished_sandwiches:
    print(sandwiches.title())

vacations = {}
active = True
while active:
    name = input("What's your name? ")
    answer = input("Where do you want to take your vacations? ")
    vacations[name] = answer
    repeat = input("Is there anyone else who wants to go? (y/n) ")
    if repeat == "n": active = False

print("\n---Vacations list---\n")
for name,answer in vacations.items():
    print(name.title() + " will go to " + answer.title() + "\n")


