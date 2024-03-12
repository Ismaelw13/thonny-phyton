#ro_pag32_ex_03

t = float(input("temperatura = "))
p = float(input("codigo = "))

if p == 1:
    c= 5 / 9 * ( t - 32 )
    print(" grados C = " , c)

if p == 2:
    f= 32 + 9 * t / 5
    print(" grados F = " , f) 