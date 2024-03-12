from math import *

k = (50 - 2 * pow(e,0.1 * 10)) / 10

print("k = ",k)

t = float(input("temps = "))

f_t = k * t + 2 * pow(e,0.1 * t)

print("f(t) = ", f_t)
