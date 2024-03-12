# ismael_Wubulikasimu_3.py

# energia necessaria

from math import*

h = float(input("alçada banyera = "))
a = 0.75
b = 1.25
t = 20

Ea = 1000 * a * b * h * 4.187 * 20

print(" energia necessaria " , Ea)

# apartat b

h = 0.2
a = 0.75
b = 1.25
t = 20

Ea = 1000 * a * b * h * 4.187 * 20

print(" energia necessaria de 200mm " , Ea)

h = 0.25
a = 0.75
b = 1.25
t = 20

Ea = 1000 * a * b * h * 4.187 * 20

print(" energia necessaria de 250mm " , Ea)

h = 0.3
a = 0.75
b = 1.25
t = 20

Ea = 1000 * a * b * h * 4.187 * 20

print(" energia necessaria de 300mm " , Ea)

h = 0.35
a = 0.75
b = 1.25
t = 20

Ea = 1000 * a * b * h * 4.187 * 20

print(" energia necessaria de 350mm " , Ea)

h = 0.40
a = 0.75
b = 1.25
t = 20

Ea = 1000 * a * b * h * 4.187 * 20

print(" energia necessaria de 400mm " , Ea)

# cost

Ea_entrada = Ea / 0.8

pes = Ea_entrada / 45790

cost = pes * (12.94 /12.5)

print ("cost en € = ", cost)