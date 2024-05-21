print("Máquina de calcular desconto de 20% para compras acima de 200 reais")

compra = float(input("Digite o valor da compra: "))
desc = compra * 0.2
valor = compra - desc
if compra >= 200:
    print("valor da compra com desconto é:" ,valor)
else:
    print("Sua compra não tem desconto ficando:" ,compra)