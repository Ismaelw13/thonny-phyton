from math import*

def númerostriangulares (n):
    t = (n*(n+1))/2
    
    print ("n =",n,"f(n) =",t)

def triangulo_for (n):
    j = 0
    for i in range (1, n+1):
        j = j + i
        print ("n =",i,"f(n) =",j)

def triangulo_while (n):
    j = 0
    i = 1
    while i <= n:
      j = j + i
      print ("n =",i,"f(n) =",j)
      i = i + 1
    
a = int(input("a = "))

for i in range (1, a+1):
    númerostriangulares (i)