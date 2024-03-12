from math import *

a = float(input("absisa punt 1 = "))
b = float(input("ordenada punt 1 = "))
c = float(input("absisa punt 2 = "))
d = float(input("ordenada punt 2 = "))

distancia_1 = sqrt(pow(a,2) + pow(b,2))
distancia_2 = sqrt(pow(c,2) + pow(d,2))

if distancia_1 < distancia_2 :
    print ("punt 1")
else:
    print("punt 2")