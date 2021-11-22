import numpy as np

a = [1, 2 ,3 ,4 ,5 ,6, 7] # declarando uma lista
np.array(a) # transformando em array com numpy
print(a)
print("\n")


b = np.arange(1, 11) # criando array no intervalo 1 a 10
print(b)
print("\n")
b2 = b.reshape((2, 5)) # alterando o array para 2 linhas e 5 colunas
print(b2)
print("\n")

c = np.concatenate((a, b)) # juntanda array a com array b
print(c)
print("\n")

for item in c: # iterando pelo array c
    print(item)
print("\n")

for itens in b2: # iterando pelo array de duas dimensões b2
    for item in itens:
        print(item)
print("\n")
