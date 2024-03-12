from random import *

n=int(input('Cantidad de datos: '))
s=0

for i in range(n):
    x=float(input('Ingrese el siguiente dato: '))
    s=s+x

p=s/n

print('El promedio es: ',p)