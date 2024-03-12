#no tots els valor son positius

from math import*

def funcio (a):
    y = 4 + sin (a) 
    
    print (y, a)
def funcio_2 (a):
    y = 4 + 230 * sin (a) 
    
    print (y,a)

a  = 0
while a <= 360:
    funcio (a)
    a = a + 45

a = 0

while a <= 360:
    funcio_2 (a)
    a = a + 45
    