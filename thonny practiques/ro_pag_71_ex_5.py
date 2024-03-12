from math import *

p = float(input("valor del depósito en euros = "))
x = float(input("intereses en meses = "))
n = float(input("número de depósitos realizados en meses = "))


a = p * ((pow(1+x,n)-1)/x)

print("valor acumulado = ", a)

