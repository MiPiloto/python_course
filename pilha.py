pilha = []

while True:
    print("Escolha uma opção:")
    print("Digite 1 para inserir na pilha;")
    print("Digite 2 para mostrar a pilha;")
    print("Digite 3 para apagar item da pilha;")
    print("Digite 4 para apagar toda a pilha;")
    print("Digite q para encerrar;")
    option = input()
    if option == "q":
        break
    elif option == "1":
        num = input("\nDigite número a ser inserido: ")
        pilha.append(num)
        print(str(num) + " inserido com sucesso!\n")
    elif option == "2":   
        for num in pilha:
            print(num)
    elif option == "3":
        num = pilha.pop(-1)
        print(str(num) + " apagado da pilha!\n")
    elif option == "4":
        pilha.clear()
        print("Pilha apagada!\n")
    else:
        print("Opção inválida.\n")
        print("Escolha uma opção:")
        print("Digite 1 para inserir na pilha;")
        print("Digite 2 para mostrar a pilha;")
        print("Digite 3 para apagar item da pilha;")
        print("Digite 4 para apagar toda a pilha;")
        print("Digite q para encerrar;")
        option = input()