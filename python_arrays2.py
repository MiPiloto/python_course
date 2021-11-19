places = ["rome","lisbon","tokyo","dublin","berlin"]
print(places)

print(sorted(places)) # organiza a lista mas não a altera
print(places)

print(sorted(places,reverse=True)) # organiza a lista mas não a altera, em ordem inversa
print(places)

places.reverse() # inverte uma lista
print(places)

places.reverse()
print(places)

places.sort() # organiza a lista, alterando-a
print(places)

places.sort(reverse=True) # organiza a lista, alterando-a em ordem inversa
print(places)

num = len(places) # len exibe a quantidade de itens da lista
print("I have " + str(num) + " cars!")

print("Os três primeiros itens da lista são " + str(places[0:3]))
print("Os três itens do meio da lista são " + str(places[1:4]))
print("Os três últimos itens da lista são " + str(places[-3:]))