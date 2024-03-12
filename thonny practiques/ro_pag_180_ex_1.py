
def conteo (n):
    a = 0
    for i in range (1, n+1):
        if n % i == 0:
            a = a + 1
            print (a,i)
    print("te un total de ", a ,"divisors")
    return a

b = 100
c = 0
d = 0
for j in range (1, b+1):
    e = conteo (j)
    if e > c:
        c = e
        d = j
        print(c)
print("el nombre amb mes divisors es: " ,d, " que te un total de ",c ," divisors ")
    