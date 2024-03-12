from math import *

radio = float(input("radio = "))
altura = float(input("altura = "))

if altura > radio :
    volumen = pi * pow(radio,2) * altura
    print("volumen = ",volumen)
else:
    print("error")