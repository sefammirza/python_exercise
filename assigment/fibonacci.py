"""
liste = []
for i in range(0, 11):
    if i <= 1:
        liste.append(i)
    else:
        liste.append(liste[i-1]+liste[i-2])
print(liste)
"""
liste = []
for i in range(0, 11):
    liste.append(i if i <= 1 else liste[i-1]+liste[i-2])
print(liste)

    