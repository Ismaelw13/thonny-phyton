from random import *

n=int(input('Ingrese el valor: '))
s=0

for i in range(1,n+1):
    c=i**2
    s=s+c
print('La suma es: ',s)
