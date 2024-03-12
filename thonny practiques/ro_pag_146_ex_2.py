from math import*

n = int(input("nombre de paquets = "))
x = 0
m = 0
p = 0
o = 0
while not n == x :
    kg = float(input(" Kg del paquet = " ))
    if kg < 10:
        m  = m + 1
    elif (kg > 10 and kg < 20) or kg == 10 :
        p = p + 1
    else :
        o = o + 1
    x = x + 1
print ( "nombre de paquets menor de 10Kg = ", m)
print ( "nombre de paquets majors de 10Kg i menors de 20Kg = ", p)
print ( "nombre de paquets majors de 20Kg = ", o)