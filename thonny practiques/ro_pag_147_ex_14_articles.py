
articles = [454, 785, 1000, 2347]
diners = 1000

for i in range (0,4):
    if diners >= articles[i] :
        x = diners // articles[i] 
        print (" pots comprar ",x, "articles ")