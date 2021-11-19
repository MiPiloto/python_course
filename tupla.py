buffet = ("arroz", "macarrão","bife","batata frita","strogonoff\n") # definindo uma tupla: lista que não aceita alteração

for food in buffet:
    print(food)

#buffet[1] = "jiló"  ERRO tentando alterar item da tupla

buffet = ("arroz", "macarrão","carne de panela","batata frita","salada\n") # re-definindo uma tupla

for food in buffet:
    print(food)

