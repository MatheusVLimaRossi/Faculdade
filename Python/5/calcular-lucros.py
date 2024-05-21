print("Máqina de calcular lucros")

nome = input("Digite o nome do produto: ")
valor = float(input("Digite o valor do produto: "))

a = valor * 0.70
b = valor * 0.50
c = valor * 0.40
d = valor * 0.30

if valor < 10:
    print("O produto é" ,nome,"com lucro de %.2f" % (a))
elif valor >= 10 and valor < 30:
    print("O produto é" ,nome,"com lucro de %.2f" % (b))
elif valor >= 30 and valor < 50:
    print("O produto é" ,nome,"com lucro de %.2f" % (c))
else: 
    print("O produto é" ,nome,"com lucro de %.2f" % (d))