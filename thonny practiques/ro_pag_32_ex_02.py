#ro_pag32_ex_02

precio = float(input("precio = "))
cantidad = float(input("kw = "))

if cantidad > 700:
    preuP = (cantidad * precio) * 0.05 + (precio * cantidad)
    print("preu total = ", preuP)
if cantidad < 700:
    preuT = cantidad * precio
    print("preu total = ", preuT)

