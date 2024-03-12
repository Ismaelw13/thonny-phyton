a = int(input("nombre de cons: "))
b = int(input("distancia entre cons en m: "))
c = int(input("amplada entre cons en cm: "))

if 10 < b and b < 30 and c < 50 and 10 < c and (a == 1 or a > 1):
    b = b * 100
    if a == 1:
        h = 0
    else:
        g = a - 1
        d = g * b
        
        e = a - 2
        f = c * e
        
        h = d - f
    print ("distancia entre el primer i unltim con es : ", h,"cm")
else:
    print("no es pot fer")