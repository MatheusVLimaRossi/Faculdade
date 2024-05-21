print("Máquina de mostrar o domínio do seu e-mail")

opcao = 0
while (opcao != 2):

    print("\n----Menu----")
    print("1 - Digitar e-mails")
    print("2 - Sair do programa")
    opcao = int(input("Escolha uma opção: "))

    if (opcao == 1):
        print("\n---- Digitar e-mails selecionado----")
        
        a = input("Digite seu e-mail: ")
        b = a.split('@')
        c = b[-1]
        print("O domínio do seu e-mail é: http://" + c)
    elif (opcao == 2):
        print("Obrigado!")
    else:
        print("ERRO! Opção inválida.")