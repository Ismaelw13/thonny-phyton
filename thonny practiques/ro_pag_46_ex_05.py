
a = int(input("nombre a = "))
b = int(input("nombre b = "))
c = int(input("nombre c = "))

if a > b :
    while not c > a :
        c = c + 3
else :
    while not a > b + c :
        a = a + 5
    print ("a = ", a)
print ("c = " , c)