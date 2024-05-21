print("Máquina de calcular segundos para horas e minutos")

s = float(input("Digite uma quantidade em segundos: "))

h = s  / 3600
m = s / 60

print("Esses segundos em horas é: %.2f" %(h))
print("Esses segundos em minutos é: %.2f" %(m))
print("Esses segundos em segundos é: %.0f" %(s))