liste = []
for i in range(0, 11):
    if i <= 1:
        liste.append(i)
    else:
        liste.append(liste[i-1]+liste[i-2])
print(liste)
    