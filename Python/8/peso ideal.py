print("Máquina de calcular seu peso ideal")

s = input("Qual seu sexo? Masculino (M) ou Feminino (F)?: ")
a = float(input("Digite sua altura: "))

pim = (72.7 * float(a)) - 58
pif = (62.1 * float(a)) - 44.7

if s == "M" or s == "m":
    print("Seu peso ideal é: %.2f" %(pim))
elif s == "F" or s == "f":
    print("Seu peso ideal é: %.2f" %(pif))
else:
    print("Sexo invalido!")