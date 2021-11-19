import build_car #importando o módulo

build_car.build_car('gol','volks',ano='97',condicao='seminovo') #chamando a função do módulo



from build_car import build_car #importando uma função específica

build_car('gol','volks',ano='97',condicao='seminovo') #chamando a função já importada



import build_car as bc #importando modulo com apelido(alias)

bc.build_car('gol','volks',ano='97',condicao='seminovo')



from build_car import* #importa todas as funções do módulo

build_car('gol','volks',ano='97',condicao='seminovo') #chamando a função já importada

