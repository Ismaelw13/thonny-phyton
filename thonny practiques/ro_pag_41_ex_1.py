
n = int(input("Introdueix el número de paquets de la bodega = "))
mayor_peso = 0

for m in range (n):
    peso = int(input("Introdueix el pes dels paquets = "))
    if peso > mayor_peso:
        mayor_peso = peso

print ("El pes més gran dels paquets és = ",mayor_peso)