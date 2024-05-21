import math

print("Máquina de calcular radiano, seno, cosseno e tangente")
a = float(input("Digite o valor do ângulo em graus: "))
rad = a * (math.pi / 180.0)
sen = math.sin (rad)
cos = math.cos (rad)
tan = math.tan (rad)

print("O valor em seno é: %.4f" % (sen))
print("O valor em cosseno é: %.4f" % (cos))
print("O valor em tangente é: %.4f" % (tan))