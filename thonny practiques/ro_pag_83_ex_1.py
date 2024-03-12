from math import *

x = int(input("dias = "))

(x,y) = divmod(x,365)

(y,z) = divmod(y,30)


print(x, "anys, ", y ," mesos i ", z , "  dies ")