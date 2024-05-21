print("Máquina de calcular gastos")

a = float(input("Digite o valor da primera conta: "))
b = float(input("Digite o valor da segunda conta: "))
c = float(input("Digite o valor da terceira conta: "))
salario = float(input("Digite seu salário: "))

soma = a + b + c 
subs = salario - soma 
print("A soma das suas contas ficou:" ,soma)

if soma <= salario:
    print("Parabéns você consegue pagar sua contas. Ainda sobrou %.2f" %(subs))
else:
    print("Salário insuficiente para pagar suas contas!")