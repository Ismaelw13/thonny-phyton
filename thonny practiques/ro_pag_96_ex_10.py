from math import *

n1 = float(input("costat 1 = "))
n2 = float(input("costat 2 = "))
n3 = float(input("costat 3 = "))

if n1 == n2 and n2 == n1 and n2 == n3:
    print("el triangulo es equilatero")
elif n1 == n2 or n1 == n3 or n2 == n3:
    print("el triangulo es isosceles")
else:
    print("el triangulo es escaleno")
    