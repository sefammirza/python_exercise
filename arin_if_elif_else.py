
age = 18
if age >= 18:
    print("Oy kullanabilirsiniz")
    
    

my_list = ['ahmet', 'mehmet', 'ebru']
if 'ahmet' in my_list:
    print('Ahmet listede var')
  

age = 15
if age >= 18:
    print('Oy kullanabilirsiniz')
else:
    print('oy kullanamazsınız')

   
  
age = 15
if age <= 2:
    print('%80 indirimli')
elif age <= 10:
    print('%50 indirimli')
else:
    print('indirim yok')
   


age = int(input('Lütfen yaşınızı giriniz:'))

if age < 0:
    age = 0
    print('Negatif sayı sıfıra çevrildi')
elif age == 0:
    print('Lütfen sıfırdan farklı bir sayı giriniz')
elif age < 18:
    print('Oy kullanamazsın')
else:
    print('Oy kullanabilirsiniz')
    
