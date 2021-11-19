for num in range(1,21): # cria lista com intervalo de 1 a 20
    print(num)

million = list(range(1,1000001)) # cria lista com intervalo de 1 a 1.000.000
#print(million)
print(min(million)) # menor valor da lista (min)
print(max(million)) # maior valor da lista (max)
print(sum(million)) # soma valores da lista (sum)

impares = list(range(1,21,2)) # range(inicio, fim, soma dois a cada item)
for value in impares:
    print(value)

tres = list(range(3,31,3)) # range(inicio, fim, soma três a cada item)
for value in tres:
    print(value)

cubos = []
for cubo in range(1,11): # loop for preenchendo array com os cubos dos números
    cubos.append(cubo**3)

print(cubos)

for cubo in cubos:
    print(cubo)

cubos2 = [value**3 for value in range(1,21)] # criando lista e preenchendo com um loop, usando list comprehension (forma resumida de sintaxe)
print(cubos2)