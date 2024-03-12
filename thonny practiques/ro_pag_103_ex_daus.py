from random import *

c=0
x=0

while not x == 3:
    x=randint(1, 6)
    c=c+1

print('Cantidad de lanzamientos hasta que salió el 3: ', c)
