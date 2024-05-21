print("Máquina de mostrar quantos valores positivos e negativos tem, mostra o menor valor deles também")
p = 0
n = 0
mv = None

while True:

    entrada = input("Insira um valor real (digite 'fim' para parar): ")

    if entrada.lower() == 'fim':
        break

    valor = float(entrada)

    if valor > 0:
        p += 1
    elif valor < 0:
        n += 1

    if mv is None or valor < mv:
        mv = valor

print("Total de valores positivos:", p)
print("Total de valores negativos:", n)
if mv is not None:
    print("Menor valor encontrado:", mv)
else:
    print("Nenhum valor foi inserido.")