from math import *

x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))

diagonal_1 = sqrt(pow(x,2) + pow(y,2))
diagonal_2 = sqrt(pow(z,2) + pow(y,2))
diagonal_3 = sqrt(pow(x,2) + pow(z,2))

if diagonal_1 == diagonal_2 == diagonal_3:
    print("tots les diagonals son iguals")
elif diagonal_1 == diagonal_2:
    if diagonal_1 > diagonal_3 and diagonal_2 > diagonal_3:
        print("diagonal_1 i diagonal_2 son iguals. El seu nombre es ", diagonal_1 )
elif diagonal_1 == diagonal_3:
    if diagonal_1 > diagonal_2 and diagonal_3 > diagonal_2:
        print("diagonal_1 i diagonal_3 son iguals. El seu nombre es ", diagonal_1 )
elif diagonal_2 == diagonal_3:
    if diagonal_3 > diagonal_1 and diagonal_2 > diagonal_1:
        print("diagonal_2 i diagonal_3 son iguals. El seu nombre es ", diagonal_2 )
elif diagonal_1 > diagonal_2 and diagonal_3:
    print("la mes gran es la diagonal 1. El seu valor es ", diagonal_1)
elif diagonal_3 > diagonal_2 and diagonal_1:
    print("la mes gran es la diagonal 3. El seu valor es ", diagonal_3)
elif diagonal_2 > diagonal_1 and diagonal_3:
    print("la mes gran es la diagonal 2. El seu valor es ", diagonal_2)

