from math import *

a = float(input("largada bloque = "))
b = float(input("anchura bloque = "))
c = float(input("altura bloque= "))

d = float(input("diamtro agugero = "))

e = sqrt( pow(a,2) + pow(b,2) + pow(c,2))

if e > d:
    print("no passa por el agujero")
else:
    print("si `pasa por el  agujero")