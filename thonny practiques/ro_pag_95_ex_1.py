from math import *

radio = float(input("radio = "))
altura = float(input("altura = "))

if altura > radio :
    volumen = pi * pow(radio,2) * altura
    print("volumen = ",volumen)
else:
    area = 2 * pi * radio * altura + 2 * pi * pow(radio,2)
    print("area = ",area)