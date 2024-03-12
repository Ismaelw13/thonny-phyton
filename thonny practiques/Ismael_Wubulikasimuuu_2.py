aaaa = int(input("any que vas neixer: "))
mm = int(input("mes que vas neixer: "))
dd = int(input("dia que vas neixer: "))

if aaaa > 2024:
    print("encara no has nascut")
elif mm > 12:
    print("no existeix aquest mes")
elif dd > 31:
    print("no existeix aquest dia")
else:
    a = aaaa + mm + dd
    b = a // 1000
    c = (a % 1000)// 100
    d = ((a % 1000) % 100)//10
    e = (((a % 1000) % 100)%10)//1
    
    f = b + c + d + e
    
    b = f // 1000
    c = (f % 1000)// 100
    d = ((f % 1000) % 100)//10
    e = (((f % 1000) % 100)%10)//1
    
    g = b + c + d + e
    
    
    b = g // 1000
    c = (g % 1000)// 100
    d = ((g % 1000) % 100)//10
    e = (((g % 1000) % 100)%10)//1
    
    h = b + c + d + e
print("la teva carta del tarot es : ",h)
    