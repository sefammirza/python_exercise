num = int(input('Lütfen bir sayı giriniz: '))

if num < 0:
    print('Negatif bir sayı girdiniz')
else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    print('Tomlam sayı:', sum)