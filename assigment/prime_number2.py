value = int(input("lütfen bir değer giriniz: "))
liste = []
for i in range(2, int(value)):
    for x in (range(2, i)):
        if (i % x)== 0:
            break
    else:
        liste.append(i)
print(liste)
        
    