from math import *

n1 = int(input("nota 1 primer alumne = "))
n2 = int(input("nota 2 primer alumne = "))
n3 = int(input("nota 3 primer alumne = "))
n2_1= int(input("nota 1 segon alumne = "))
n2_2= int(input("nota 2 segon alumne = "))
n2_3= int(input("nota 3 segon alumne = "))

if n1 == n2 == n3:
    n1 = n1 + n2
    print("tots les notes del primer alumne son iguals = ",n1)
elif n1 == n2:
    if n1 > n3 and n2 > n3:
        n1 = n1 + n2
        print("la nota final del primer alumne es =", n1 )
elif n1 == n3:
    if n1 > n2 and n3 > n2:
        n1 = n1 + n3 
        print("la nota final del primer alumne es =", n1 )
elif n2 == n3:
    if n3 > n1 and n2 > n1:
        n2 = n2 + n3 
        print("la nota final del primer alumne es =", n2 )
elif n1 > n2 and n3:
    if n2 > n3:
        n1 = n1 + n2
    else:
        n1 = n1 + n3
    print("la nota final del primer alumne es =", n1)
elif n2 > n1 and n3:
    if n1 > n3:
        n2 = n1 + n2
    else:
        n2 = n2 + n3
    print("la nota final del primer alumne es =", n2)
elif n3 > n2 and n1:
    if n2 > n1:
        n3 = n3 + n2
    else:
        n3 = n1 + n3
    print("la nota final del primer alumne es =", n3)
    

if n2_1 == n2_2 == n2_3:
    n2_1 = n2_1 + n2_2
    print("tots les notes del segon alumne son iguals = ",n2_1)
elif n2_1 == n2_2:
    if n2_1 > n3 and n2_2 > n2_3:
        n2_1 = n2_1 + n2_2
        print("la nota final del segon alumne es =", n2_1 )
elif n2_1 == n2_3:
    if n2_1 > n2_2 and n2_3 > n2_2:
        n2_1 = n2_1 + n2_3 
        print("la nota final del segon alumne es =", n2_1 )
elif n2_2 == n2_3:
    if n2_3 > n2_1 and n2_2 > n2_1:
        n2 = n2 + n3 
        print("la nota final del segon alumne es =", n2_2 )
elif n2_1 > n2_2 and n2_3:
    if n2_2 > n2_3:
        n2_1 = n2_1 + n2_2
    else:
        n2_1 = n2_1 + n2_3
    print("la nota final del segon alumne es =", n2_1)
elif n2_2 > n2_1 and n2_3:
    if n2_1 > n2_3:
        n2_2 = n2_1 + n2_2
    else:
        n2_2 = n2_2 + n2_3
    print("la nota final del segon alumne es =", n2_2)
elif n2_3 > n2_2 and n2_1:
    if n2_2 > n2_1:
        n2_3 = n2_3 + n2_2
    else:
        n2_3 = n2_1 + n2_3
    print("la nota final del segon alumne es =", n2_3)
elif n2_1 or n2_2 or n2_3 > n1 or n2 or n3:
    print("el segon alumne es el q te millor notes")
elif n1 or n2 or n3 > n2_1 or n2_2 or n2_3:
    print("el primer alumne es el q te millor notes")
