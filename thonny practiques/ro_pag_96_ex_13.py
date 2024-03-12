from math import *

a = float(input("trabajador 1 horas trabajadas = "))
b = float(input("trabajador 1 salario por horas = "))
c = float(input("trabajador 1 descuento  = "))

d = float(input("trabajador 2 horas trabajadas = "))
e = float(input("trabajador 2 salario por horas = "))
f = float(input("trabajador 2 descuento  = "))

g = float(input("trabajador 3 horas trabajadas = "))
h = float(input("trabajador 3 salario por horas = "))
i = float(input("trabajador 3 descuento = "))

salario_1 = a  * b - c
salario_2 = d * e - f
salario_3 = g * h - i

if salario_1 > salario_2 and salario_1 > salario_3 :
    print ("el trabajador 1 es el que a recibido mayor salario con ", salario_1, "€")

if salario_2 > salario_1 and salario_2 > salario_3 :
    print ("el trabajador 2 es el que a recibido mayor salario con ", salario_2, "€")

else:
    print ("el trabajador 3 es el que a recibido mayor salario con ", salario_3, "€")