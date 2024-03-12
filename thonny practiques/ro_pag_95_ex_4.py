from math import *

x = int(input("nombre de dues xifres = "))
y = x // 10
z = x % 10

if (y + z) % 2 == 0:
    print("es parell")
else:
    print("es imparell")
