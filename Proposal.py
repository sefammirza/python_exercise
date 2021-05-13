    
def indirim(n):  
    oneri1 = (n-15)*10*0.6
    oneri2 = n*10*0.52

    print("1. öneri: " + str(oneri1))
    print("2. öneri: " + str(oneri2))

    if oneri1 < oneri2:
        print("1. Öneriyi seçmelisiniz")
    else:
        print("2. Öneriyi seçmelisiniz")
        
indirim(90 )