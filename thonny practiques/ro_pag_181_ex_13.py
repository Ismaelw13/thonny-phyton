from math import*

def convertirpolar (x,y):
    r = sqrt (pow(x,2) + pow(y,2))
    t = atan (y/x)
    t = t * (360/(2 * pi)) 
    print(r,t)
    
def convertircartesiana (r,t):
    t = t * ((2 * pi)/360)
    x = r * cos(t)
    y = r * sin(t)
    print (x,y)
    
a = int(input("a = "))
 

if a == 1:
    b = float(input("x = "))
    c = float(input("y = "))
    convertirpolar (b,c)
elif a == 2:
    b = float(input("r = "))
    c = float(input("t = "))
    convertircartesiana (b,c)
else:
    print("adeu")