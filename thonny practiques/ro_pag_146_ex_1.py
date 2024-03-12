from math import*

n = int(input("Introdueix el número de paquets de la bodega = "))
mayor_peso = 0
menor_peso = 0
while n > 0:
    peso = int(input("Introdueix el pes dels paquets = "))
    if peso > mayor_peso:
        mayor_peso = peso
    if peso < menor_peso :
        menor_peso = peso
    n = n - 1

print ("El pes més gran dels paquets és = ",mayor_peso)
print ("El pes més petit dels paquets és = ",menor_peso)