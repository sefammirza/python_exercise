def faktoriyel(a):
    if a == 0:
        return 1
    else:
        return a * faktoriyel(a-1)
    
a = int(input('Lütfen bir sayı giriniz:'))
print(faktoriyel(a))