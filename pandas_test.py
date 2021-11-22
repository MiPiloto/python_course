# importando Pandas
import pandas as pd


# criando lista de 1 a 10
a = list(range(1, 11))

# transformando em uma Serie com Pandas e adicionando indices(opcional)
a = pd.Series(a, index = ["a","b","c","d","e","f","g","h","i","j"]) 
print(a)

# criando um dicionário
b = {
    "bruce":{"first":"cave","second":"mansion","third":"rooftops"},
    "clark":{"first":"krypton","second":"daily-bugle","third":"phone-cabin"},
    "peter":{"first":"skyscrapper","second":"may's house","third":"laboratory"},
}

# transformando o dicionário em um DataFrame com Pandas
b1 = pd.DataFrame(b) 
print(b1)
print("\nTransposed DataFrame:\n")

# transposição de linhas em colunas com Pandas
bt = b1.T
print(bt)

# selecionando linhas para exibição por indice com iloc
print(b1.iloc[0])
print(b1.iloc[2])

# selecionando linhas para exibição por nome com loc
print(bt.loc["bruce"])
print(b1.loc["second"])