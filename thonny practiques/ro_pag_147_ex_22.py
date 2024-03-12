from random import*

x = 0
y = 0
z = 0

i = 0
while x < 20 and y < 20 and z < 20:
    e = randint (1,4)
    if e == 1 :
        x = x + 0
    elif e == 2:
        x = x + 0.5
    elif e == 3:
        x = x + 1
    elif e == 4:
        x = x - 0.5
    
    f = randint (1,4) 
    if f == 1 :
        y = y + 0
    elif f == 2:
        y = y + 0.5
    elif f == 3:
        y = y + 1
    elif f == 4:
        y = y - 0.5
    
    g = randint (1,4)
    
    if g == 1 :
        z = z + 0
    elif g == 2:
        z = z + 0.5
    elif g == 3:
        z = z + 1
    elif g == 4:
        z = z - 0.5
    
    i = i + 1
    print(i,"intents",x, "espai recorregut")
    print(i,"intents",y, "espai recorregut")
    print(i,"intents",z, "espai recorregut")

if x > 20 or x == 20:
    print("granota 1 guanyadora")
elif y > 20 or y == 20:
    print("granota 2 guanyadora")
elif z > 20 or z == 20:
    print("granota 3 guanyadora")    
    