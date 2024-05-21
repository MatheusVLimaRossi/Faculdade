print("Calculadora")

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
op = input("Digite a função que deseja, sendo elas ('+' '-' '*' ou '/'): ")

mais = a + b
menos = a - b
vezes = a * b
div = a / b

if op == '+':
    print("A soma dos números é: %.2f" % (mais))
elif op == '-':
    print("A subtração dos números é: %.2f" % (menos))
elif op == '*':
    print("A multiplicação dos números é: %.2f" % (vezes))
elif op == '/':
    print("A divisão dos números é: %.2f" % (div))
else:
    print("Função não válida")