liste = [75 ,73,60,100,120,130]
kar = []
for i in range(len(liste) -1):
    for x in range(i+1,len(liste)):
        kar.append(liste[x]-liste[i])
print(kar)
print(max(kar))