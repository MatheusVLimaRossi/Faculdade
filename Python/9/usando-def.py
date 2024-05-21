def maiorNum(n1, n2):
    if (n1 > n2):
        print("O maior número é:" ,(n1))
        print("")
    else:
        print("O maior número é:" ,(n2))
        print("")

def testaRange(n1):
    if (n1 >= 1 and n1 <= 9):
        print("1\n")
    else:
        print("0\n")

opcao = 0
while (opcao!=9):
    print("---- Menu ----")
    print("1 - Maior de 2 números")
    print("2 - Teste de números")
    print("9 - Sair")
    opcao = int(input("Digite opção: "))
    if (opcao == 1):
        print("\n ---- Maior de 2 números ----")
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        maiorNum (n1, n2)
    elif (opcao == 2):
        print("\n ---- Teste de números ----")
        n1 = int(input("Digite um número: "))
        testaRange (n1)
    elif (opcao == 9):
        print("Programa encerrado!")
    else:
        print("ERRO! Número incorreto \n")