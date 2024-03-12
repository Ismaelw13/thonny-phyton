from math import *

catidad_de_dolares = int(input("nombre en dolars = "))

dolares_en_billetes_de_100 = catidad_de_dolares // 100
dolares_en_billetes_de_50 = (catidad_de_dolares % 100) // 50
dolares_en_billetes_de_20 = ((catidad_de_dolares % 100) % 50) // 20
dolares_en_billetes_de_10 = (((catidad_de_dolares % 100) % 50) % 20) // 10
dolares_en_billetes_de_5 = ((((catidad_de_dolares % 100) % 50) % 20) % 10) // 5
dolares_en_billetes_de_1 = (((((catidad_de_dolares % 100) % 50) % 20) % 10) % 5) // 1

print ("dolares_en_billetes_de_100 = ", dolares_en_billetes_de_100)
print ("dolares_en_billetes_de_50 = ", dolares_en_billetes_de_50)
print ("dolares_en_billetes_de_20 = ", dolares_en_billetes_de_20)
print ("dolares_en_billetes_de_10 = ", dolares_en_billetes_de_10)
print ("dolares_en_billetes_de_5 = ", dolares_en_billetes_de_5)
print ("dolares_en_billetes_de_1 = ", dolares_en_billetes_de_1)