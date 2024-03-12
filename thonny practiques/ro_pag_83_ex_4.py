from math import *

numero_original = int(input("nombre de tres xifres = "))

nombre_centenes = numero_original // 100
nombre_desenes = (numero_original % 100) // 10
nombre_unitari = numero_original % 10

nombre_al_reves = (nombre_unitari * 100) + (nombre_desenes * 10) + (nombre_centenes * 1)

print("el nombre al reves es = ",nombre_al_reves)