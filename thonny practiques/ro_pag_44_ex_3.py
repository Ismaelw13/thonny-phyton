
        
a = int(input("nombre a: "))
b = int(input("nombre b: "))
c = int(input("nombre c: "))

r = 0

while not a < b or c < 0:
    
    if b % 2 == 0:
        b = b + 1
    else :
        r = r + c
        b = b + 1

print("El valor de r es:", r)
