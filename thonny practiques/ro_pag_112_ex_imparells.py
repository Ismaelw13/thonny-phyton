from random import *

n=int(input('Ingrese la cantidad de impares: '))
s=0
imp=1

for i in range(n):
    s = s + imp
    imp = imp + 2

if s == pow(n , 2):
    print("Verdadero")

else:
    print("Falso")