# ismael_Wubulikasimu_1.py

from math import*

x = 0
while x == 0:
    x = float(input("sou anual en € ="))
    if x < 10000:
        x = x - x * 0.05
        print( " tipus impositiu del 5% que es", x )
    elif (x > 10000 and x < 20000) or x == 10000:
        x = x - x * 0.15
        print( " tipus impositiu del 15% que es", x)
    elif (x > 20000 and x < 35000) or x == 20000:
        x = x - x * 0.20
        print( " tipus impositiu del 20% que es ", x)
    elif (x > 35000 and x < 60000) or x == 35000:
        x = x - x * 0.30
        print( " tipus impositiu del 30% que es ", x)
    else:
        x = x - x * 0.45
        print( " tipus impositiu del 45% que es", x)