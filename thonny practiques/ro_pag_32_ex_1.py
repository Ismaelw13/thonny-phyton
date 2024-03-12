#Ro_pag32_ex_1

radio = float(input("radio = "))
altura = float(input("altura = "))

if altura > radio:
    volum = 3.1416 * radio**2 * altura
    print("volum = ", volum)
if altura < radio:
    area = 2 * 3.1416 * radio * altura + 2 * 3.1416 * radio**2
    print("area = ", area)
    