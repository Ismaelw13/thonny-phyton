def gelat_avellana (f):
    a = 2.25
    if a == f:
        print("no hi ha canvi el valor es exacte")
    elif f > a:
        f = f - a
        g = f // 0.50
        h = (f % 0.50) // 0.20
        i = ((f % 0.50) % 0.20) // 0.05
        j = (((f % 0.50) % 0.20) % 0.05) // 0.02
        k = ((((f % 0.50) % 0.20) % 0.05) % 0.02) // 0.01
        print ("monedes de 50 centims € = ",g,"monedes de 20 centims € = ",h,"monedes de 5 centims € = ",i,"monedes de 2 centims € = ",j,"monedes de 1 centims € = ",k)
    else:
        print ("falten diners en €")
def pastis_ametlla (f):
    a = 1.75
    if a == f:
        print("no hi ha canvi el valor es exacte")
    elif f > a:
        f = f - a
        g = f // 0.50
        h = (f % 0.50) // 0.20
        i = ((f % 0.50) % 0.20) // 0.05
        j = (((f % 0.50) % 0.20) % 0.05) // 0.02
        k = ((((f % 0.50) % 0.20) % 0.05) % 0.02) // 0.01
        print ("monedes de 50 centims € = ",g,"monedes de 20 centims € = ",h,"monedes de 5 centims € = ",i,"monedes de 2 centims € = ",j,"monedes de 1 centims € = ",k)
    else:
        print ("falten diners en €")
l = int(input("quin opcio vols 1: gelat de avellana o 2: pastis de ametlla = ")) 
a = int(input("quantitat de monedes de 50 centims € = "))
b = int(input("quantitat de monedes de 20 centims € = "))
c = int(input("quantitat de monedes de 5 centims € = "))
d = int(input("quantitat de monedes de 2 centims € = "))
e = int(input("quantitat de monedes de 1 centims € = "))
f = (a*0.50)+(b*0.20)+(c*0.05)+(d*0.02)+(e*0.01)

if l == 1:
    gelat_avellana (f)
elif l == 2:
    pastis_ametlla (f)
else:
    print("no existeix la opcio")
