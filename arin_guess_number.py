import random
xnum = random.randint(1, 100)

num = int(input('Lütfen 1 ile 100 arasında bir sayı girin: '))

while num != xnum:
    if num < xnum:
        print(f'{num} daha büyük bir sayı giriniz')
        num = int(input())
    else:
        print(f'{num} daha küçük bir sayı giriniz')
        num = int(input())
        
print(f' Tebrikler {num} yakaladınız!')