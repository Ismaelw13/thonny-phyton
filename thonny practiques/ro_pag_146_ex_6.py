from math import*

n = int(input("personas votants = "))
m = 0
p = 0
b = 0
c = 0
d = 0
e = 0

while m < n:
    
    a = int(input("vot = "))
    
    if a == 0:
        p = p + 1
    elif a == 1:
        b = b + 1
    elif a == 2:
        c = c + 1
    elif a == 3:
        d = d + 1
    else:
        e = e + 1
    
    m = m + 1


print ("voto en blanco = ", p)
print ("votos primer candidato = ", b)
print ("votos segundo candidato = ", c)
print ("votos tercer candidato = ", d)
print ("voto nulos = ", e)