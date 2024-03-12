from math import *

a = float(input("productes comprats = "))
b = float(input("precio unitario en € = "))

if a < 5 or a == 5:
    c = b * a
    print ( "precio total en € = ",c)
elif a > 5 and a < 10:
    b = b * 0.95
    c = b * a
    print ( "precio total en € = ",c)
elif a > 10 or a == 10:
    b = b * 0.92
    c = b * a
    print ( "precio total en € = ",c)
    