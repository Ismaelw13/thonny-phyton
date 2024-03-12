from random import *

n=int(input('Ingrese el valor final: '))
s=0
i=1

while i < n or i == n:
    c = pow(i,2)
    s = s+c
    i = i+1

print('La suma es: ', s)
