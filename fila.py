fila = []

while True:
    print("Escolha uma opção:")
    print("Digite 1 para inserir na fila;")
    print("Digite 2 para mostrar a fila;")
    print("Digite 3 para apagar item da fila;")
    print("Digite 4 para apagar toda a fila;")
    print("Digite q para encerrar;")
    option = input()
    if option == "q":
        break
    elif option == "1":
        num = input("\nDigite número a ser inserido: ")
        fila.append(num)
        print(str(num) + " inserido com sucesso!\n")
    elif option == "2":   
        for num in fila:
            print(num)
    elif option == "3":
        num = fila.pop(0)
        print(str(num) + " apagado da fila!\n")
    elif option == "4":
        fila.clear()
        print("Fila apagada!\n")
    else:
        print("Opção inválida.\n")
        print("Escolha uma opção:")
        print("Digite 1 para inserir na fila;")
        print("Digite 2 para mostrar a fila;")
        print("Digite 3 para apagar item da fila;")
        print("Digite 4 para apagar toda a fila;")
        print("Digite q para encerrar;")
        option = input()




