from math import*

x = int(input( "nombre = " ))
n = 0
p = 0
m = 0
while x > n:
    p = p + 1
    m = pow( p , 2 )
    n = n + m
    print ( n)
print ( " necessitamos ", p , "terminos para superar" , x ,)