print("Máquina de calcular total de dias que uma pessoa viveu")
anos = int(input("Digite sua idade em anos: "))
meses = int(input("Digite sua idade em meses: "))
dias = int(input("Digite sua idade em dias: "))
valor1 = anos * 365
valor2 = meses * 30
calculo = valor1 + valor2 + dias 
print("O total de dias que você viveu foi de:" ,calculo)