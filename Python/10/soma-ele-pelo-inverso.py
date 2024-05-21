print("Máquina de calcular uma número mais o inverso dele")

opcao = 0
while (opcao != 2):

    print("\n----Menu----")
    print("1 - Fazer o calculo")
    print("2 - Sair do programa")
    opcao = int(input("Escolha uma opção: "))

    if (opcao == 1):
        print("\n---- Fazer calculo selecionado ----")

        n1 = (input("Digite um número inteiro com três algarismos: "))
        inverso = " "
        for x in n1:
            inverso = x + inverso
        print("O número inverso é:" ,inverso)

        n1 = int(n1)
        inverso = int(inverso)

        soma = n1 + inverso

        print("\nA soma de",n1,"+",inverso,"é:" ,soma)
    elif (opcao == 2):
        print("Obrigado!")
    else:
        print("ERRO! Opção inválida.")
