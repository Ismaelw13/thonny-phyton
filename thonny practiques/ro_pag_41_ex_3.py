n = int(input("determine la summa = "))
anterior = 0
numero = 1
seguent = 0

for i in range (n):
    seguent = numero + anterior
    anterior =  numero
    numero = seguent

print (" numero = ", seguent)