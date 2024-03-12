n = int(input("nombre = "))  # Número de términos a utilizar (cuanto mayor, mejor será la aproximación)
pi = 0  # Inicializamos la aproximación a 0

for i in range(n):
    termino = ((-1) ** i) / (2 * i + 1)
    pi += termino

pi *= 4  # Multiplicamos por 4 para obtener una aproximación de π

print("pi = ", pi)
