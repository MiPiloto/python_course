pizzas = ["marguerita","atum","frango com catupity","calabresa","alface"]
for pizza in pizzas: # testando laço for
    print("Eu gosto de pizza de " + pizza + "!")

print("Pizza é a melhor coisa do mundo!\n")

animals = ["cachorro","lobo","gato"]
for animal in animals: # laço for com mais de uma linha, exemplo de indentação
    print(animal.title() + " seria um ótimo animal de estimação!")
    print("Eu gosto de " + animal + "s!\n")

friend_pizzas = pizzas[:]

pizzas.append("siciliana")
friend_pizzas.insert(2,"rúcula")

print("Minhas pizzas favoritas são:\n")
for pizza in pizzas:
    print(pizza)

print("\n")

print("As pizzas favoritas dos meus amigos são:\n")
for friend_pizza in friend_pizzas:
    print(friend_pizza)

