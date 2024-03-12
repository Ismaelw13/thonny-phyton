#RO_P025_02_area_cilindre

altura= float(input("Altura en metres ="))

volum= float(input("Volum en litres ="))

volum_en_metres_cubics= volum/1000

diametre= ((volum_en_metres_cubics*4)/(3.1416*altura))**0.5

print ("Volum en metres cúbics =", volum_en_metres_cubics)
print ("Diàmetre de la base =", diametre)