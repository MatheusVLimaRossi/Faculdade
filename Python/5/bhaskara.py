print("Máquina de calcular bhaskara - valor de delta + x¹ e x²")

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
delta = (b*b) - (4*a*c)
neg = delta * (-1)
print("O valor de delta é:" ,delta)

x1 = ((b*-1) + delta**0.5) / (2*a)
print("O valor de x¹ é:" ,x1)
x2 = ((b*-1) - delta**0.5) / (2*a)
print("O valor de x² é:" ,x2)

if a == 0:
    print("Não é equação do segundo grau")
elif delta == neg:
    print("Não há raízes reais")
else:
    print("Tudo certo!")