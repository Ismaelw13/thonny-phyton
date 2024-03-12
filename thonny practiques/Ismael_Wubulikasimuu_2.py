
files = int(input("nombre de files = "))
a = "*"
b = 0
columnes = 0
for i in range (1, files+1):

    for j in range (1):
        columnes = columnes + 1
        b = a * columnes
        print (b)



columnes = files
for i in range (1, files+1):

    for j in range (1):
        b = a * columnes
        print (b)
        columnes = columnes - 1

