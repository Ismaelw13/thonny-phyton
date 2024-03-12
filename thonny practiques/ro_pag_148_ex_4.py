from random import*

n = int(input("intents : "))
x = 0

for i in range (1,n+1):
    y = randint(1,6)
    if y == 1:
        x = x + 1
    elif y == 2:
        x = x-2
    elif y == 3:
        x = x-2
    elif y == 4:
        x = x-2
    elif y == 5:
        x = x-2
    else:
        x = x + 5
    print ("intent ", i, "dolars que tinc", x)