from math import *

n1 = int(input("nota 1 = "))
n2 = int(input("nota 2 = "))
n3 = int(input("nota 3 = "))

if n1 > n2 and n1 > n3:
    print("la nota major es", n1)
elif n2 > n1 and n2 > n3:
    print("la nota major es", n2)
elif n3 > n2 and n3 > n1:
    print("la nota major es", n3)


if n1 < n2 and n1 < n3:
    print("la nota menor es", n1)
elif n2 < n1 and n2 < n3:
    print("la nota menor es", n2)
else:
    print("la nota menor es", n3)