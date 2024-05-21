print("Máquina para saber sua classe eleitoral")

idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Não eleitor")
elif idade >= 18 and idade <=65:
    print("Eleitor obrigatório")
else:
    print("Eleitor facultativo")