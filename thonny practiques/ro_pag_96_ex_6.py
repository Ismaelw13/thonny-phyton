from math import *

x = float(input("nombre de Kwh = "))
y = float(input("preu en €/Kwh = "))

if x > 700:
    y = y * 1.05
z = x * y
print ("preu total = ",z)