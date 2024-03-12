from math import*

a = float(input("primer nombre = "))
b = float(input("segon nombre = "))
c = float(input("tercer nombre = "))

if (pow(b,2) - 4 * a * c) < 0:
    print("la solucio es imagimaria")
else:
    d = (- b + sqrt(pow(b,2) - 4 * a * c))/ 2 * a
    print("primera solució : ", d)
    
    d = (- b - sqrt(pow(b,2) - 4 * a * c))/ 2 * a
    print ("primera solució : ", d)