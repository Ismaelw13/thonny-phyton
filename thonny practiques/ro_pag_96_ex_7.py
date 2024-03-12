from math import *

t = float(input("temperatura = "))
p = float(input("codigo (1 o 2) = "))

if p == 1 :
    c = 5 / 9 * ( t - 32 )
    print("grados c = ", c)
elif p == 2 :
    f = 32 + 9 * t / 5
    print("grados f = ", f)
else:
    print("error")