
a = int(input("nombre a = "))
b = int(input("nombre b = "))
c = int(input("nombre c = "))
d = int(input("nombre d = "))

if ( a > 0 ) or ( b > a ) and (not c == d ):
    a = c
    b = 0
else :
    c = c + d
    if c == 0 :
        c = c + b
    else :
        c = c - a
    b = a + c + d
print ( " a = ", a , " b = ", b, " c = ", c, " d = ", d)