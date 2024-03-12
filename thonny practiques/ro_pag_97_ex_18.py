from math import *

a = float(input("peso = "))
b = float(input("talla = "))

IMC = a / pow(b,2)

if IMC < 20:
    print("desnutrido")
elif IMC == 20 and IMC < 25:
    print("normal")
elif IMC == 25 and IMC < 30:
    print("sobrepeso")
elif IMC == 30 and IMC < 35:
    print("obesidad grado 1")
elif IMC == 35 and IMC < 40:
    print("obesidad grado 2")
else:
    print("obesidad grado 3")

