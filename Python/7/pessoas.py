
h = 0
m = 0
ah = 0
am = 0

p = int(input("Insira o número total de pessoas: "))

for i in range(p):
    sexo = input("Insira o sexo da pessoa (M/F): ").upper()
    altura = float(input("Insira a altura da pessoa (em metros): "))

    if sexo == 'M':
        h += 1
        ah += altura
    elif sexo == 'F':
        m += 1
        am += altura
    else:
        print("Sexo inválido. Por favor, insira 'M' para masculino ou 'F' para feminino.")

mh = ah / h if h > 0 else 0
mm = am / m if m > 0 else 0

print("Altura média dos homens:", mh)
print("Altura média das mulheres:", mm)