from math import *

x = int(input("nombre de tres xifres = "))
y = int(input("nombre de tres xifres = "))

x = (x % 100) // 10
y = (y % 100) // 10

z = x + y
print("suma de les xifres centrals = ", z )
