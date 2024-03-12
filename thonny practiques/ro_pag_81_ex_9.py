from math import *

a = float(input("nombre x del punt P = "))
b = float(input("nombre y del punt P = "))

c = float(input("nombre x del punt Q = "))
d = float(input("nombre y del punt Q = "))

# formula del punto P al punto Q
x = sqrt(pow(c-a,2)+pow(d-b,2))
# del punto P a la coordenada (0,0)
y = sqrt(pow(0-a,2)+pow(0-b,2))
# del punto Q a la coordenada (0,0)
z = sqrt(pow(0-c,2)+pow(0-d,2))

# formula area triangulo
A = (x+y+z)/2

print("area trianguo = ", A)