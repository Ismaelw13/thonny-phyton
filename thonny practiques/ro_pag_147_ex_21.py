from random import*
x=0
i=0
while not x == 10 :
    d=randint(1,2)
    i=i+1
    if d==1:
        x=x+1
    else:
        x=x-1


print(x)
print('Cantidad de intentos: ',i)
