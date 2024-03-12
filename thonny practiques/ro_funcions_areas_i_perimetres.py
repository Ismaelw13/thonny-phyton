from math import*

def cuadrado(a):
    A = pow(a,2)
    P = 4 * a
    return [A, P]
def trangulo (a, b, c, h):
    A = (b * h) / 2
    P = a + b + c
    return [A, P]
def rectángulo (a, b) :
    A = a * b
    P = 2*(a + b)
    return [A,P]
def paralelogramo (a, b, h) :
    A = b * h
    P = 2*(a + b)
    return [A,P]
def rombo (a, b, D, d) :
    A = (D * d) / 2
    P = 4*a
    return [A,P]
def cometa (a, b, D, d) :
    A = (D * d) / 2
    P = 2*(a + b)
    return [A,P]
def trapecio (a, b, B, c, h) :
    A = ((B * b) * h)/ 2
    P = B + b + a + c
    return [A,P]
def circulo (r) :
    A = pi * pow(r,2)
    P = 2*pi * r
    return [A,P]
def poligonoregular (a, n, b) :
    A = (P*a)/ 2
    P = n * b
    return [A,P]
def coronacircular (r, R) :
    A = pi * (pow(R,2) - pow(r,2))
    return [A]
def sectorcircular (R, n) :
    A = (pi * pow(R,2) * n) / 360
    return [A]
def cubo (a) :
    A = 6 * pow(a,2)
    V = pow(a,3)
    return [A,V]
def cilindre (R, h) :
    A = 2 * pi * R(h + R)
    V = pi * pow(R,2) * h
    return [A,V]
def ortoedro (a, b, c) :
    A = 2 * (a*b+a*c+b*c)
    V = a*b*c
    return [A,V]
def prismarecto (a, P, h, ab) :
    A = P * (h+a)
    V = ab * h
    return [A,V]
def cono (R, g, h) :
    A = pi * R *(R+g)
    V = (pi* pow(R,2) *h)/3
    return [A,V]
def troncodecono (r,R,h) :
    A = pi * (g* (r + R) + pow(r,2) +pow(R,2))
    V = (pi * h * (pow(R,2) + pow(r,2) + r*R))/3 
    return [A,V]
def esfera (R) :
    A = 4 * pi *pow(R,2)
    V = (4 * pi * pow(R,3))/3
    return [A,V]
def piramide (a, b, c, h, p) :
    A = (P *(a+b))/2
    V = (c * h)/3
    return [A,V]
def tetraedroregular (a) :
    A = sqrt(3) * pow(a,2)
    V = (sqt(2) * pow(a,3))/12
    return [A,V]
def octaedroregular (a) :
    A = 2 * sqrt(3) * pow(a,2)
    V = (sqrt(2) * pow(a,3))/3
    return [A,V]
def troncodepiramide (P,p,a,A,Ab,h) :
    A = ((p+P)/2) * a + A + Ab
    V = ((A + Ab + sqrt(A * Ab))* h)/3
    return [A,V]
def casqueteesferico (R,h) :
    A = 2*pi*R*h
    V = (pi*pow(h,2) *(3*R-h))/3
    return [A,V]
def husocuñaesferica (R,n) :
    A = (4 * pi*pow(R,2) * n)/360
    V = (4*pi*pow(R,3)* n)/3*360
    return [A,V]
def zonaoseguimientoesfeico (R,h,r,s) :
    A = 2*pi*R*h
    V = (pi*h*(pow(h,2) + 3*pow(r,2)+3*pow(s,2)))/6
    return [A,V]

sortida = 1
while sortida == 1:
    print("1 =cuadrado")
    print("2 = trangulo ")
    print("3 = rectángulo")
    print("4 = paralelogramo")
    print("5 = rombo")
    print("6 = cometa")
    print("7 = trapecio")
    print("8 = circulo")
    print("9 = poligonoregular")
    print("10 = coronacircular")
    print("11 = sectorcircular")
    print("12 = cubo")
    print("13 = cilindre")
    print("14 = ortoedro")
    print("15 = prismarecto")
    print("16 = cono")
    print("17 = troncodecono")
    print("18 = esfera")
    print("19 = piramide")
    print("20 = tetraedroregular")
    print("21 = octaedroregular")
    print("22 = troncodepiramide")
    print("23 = casqueteesferico")
    print("24 = husocuñaesferica")
    print("25 = zonaoseguimientoesfeico")
    
    if
    
    sortida = 3
    
    