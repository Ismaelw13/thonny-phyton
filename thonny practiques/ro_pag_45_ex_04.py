
a = int(input("nombre a = "))
b = int(input("nombre b = "))
x = 0

if a < 5 :
    x = x + a - b
else :
    while not x > b:
        x = x + a
print ("x = ", x)