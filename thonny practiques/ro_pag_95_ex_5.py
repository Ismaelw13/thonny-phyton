from math import *

x = float(input("nombre = "))

if x % 1 == 0:
    print ("x es un nombre enter")
    if x % 7 == 0:
        print("x es un nombre multiple de 7")
    else:
        print("x no es un multiple de 7")
else:
    print("x no es un nombre enter")
    print("x no es un multiple de 7")