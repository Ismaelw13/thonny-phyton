
n = int(input("nombre n = "))
s = 0

for i in range (1, n + 1 ) :
    k = (2 * i) - 1
    s = s + k
    
if s == (n ** 2) :
    print ("verdadero")
else :
    print ( "falso" )