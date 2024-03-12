from math import *

diagonal = 5
angle = 40

angle_radiants = angle * (pi/180)

a = diagonal * sin(angle_radiants)
b = diagonal * cos(angle_radiants)

area = (a * b) / 2
print("area =", area)