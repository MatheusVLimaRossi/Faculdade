print("Máquina de calcular o total que você ganha")

turno = input("Digite o turno que trabalha (N - noturo; M - matutino ou V - vespertino): ")
horas = float(input("Digite as horas trabalhadas: "))

n = horas * 45
ambas = horas * 37.50

if (turno == 'N'):
    print("O total que você vai ganhar é de: %.2f" %(n))
else:
    print("O total que você vai ganhar é de: %.2f" %(ambas))