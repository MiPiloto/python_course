names=["john","jack","jill"] # criando array
print(names[0].title())
print(names[1].title())
print(names[2].title())


message = "Hello, my friend " + names[0].title()
print(message)
message = "Hello, my friend " + names[1].title()
print(message)
message = "Hello, my friend " + names[2].title()
print(message)

dinner_invite = "Would you like to go out for dinner, " + names[0].title() + " ?"
print(dinner_invite)
dinner_invite = "Would you like to go out for dinner, " + names[1].title() + " ?"
print(dinner_invite)
dinner_invite = "Would you like to go out for dinner, " + names[2].title() + " ?"
print(dinner_invite)

print("Too bad, " + names[2].title() + " is busy today.")
names[2] = "clark" # alterando valor de item dentro de array

dinner_invite = "Would you like to go out for dinner, " + names[2].title() + " ?"
print(dinner_invite)

print("Found a bigger table!")
names.insert(0,"fin") # inserindo itens em posições específicas
names.insert(2,"greg")
names.append("kim") # inserindo item no final da lista

print(names)
print("Only two people can come, I' sorry!")

first = names.pop() # remove item do final da lista e armazena em variável
print("There's no room for you " + first)
second = names.pop()
print("There's no room for you " + second)
third = names.pop(0) # remove item do índice especificado e armazena em variável
print("There's no room for you " + third)
fourth = names.pop(2)
print("There's no room for you " + fourth)

print("Let's go " + names[0].title() + " and " + names[1].title() + "!")

del names[1] # remove item da lista
del names[0]

print(names)