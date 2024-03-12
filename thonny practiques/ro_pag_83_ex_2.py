from math import *

x = int(input("dias = "))

(x,y) = divmod(x,30)

(y,z) = divmod(y,4)

print(x, "mesos, ", y ," semanas i ", z , "  dies ")