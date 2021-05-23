"""
"""

"""def func(username, age=25):
    print(f'Merhaba {username} , {age} yaşındasınız')
    
func('Arin')"""

"""
"""
 
"""    
def func():
    pass 
func()
"""
"""
mylist = [1, 4, 7, 3, 9, 4]

myset = set(mylist)
print(myset)
print(type(myset))
print(sum(myset))
"""
"""


"""
"""
cikar = lambda a, b : a + b

print(cikar(10, 8))
"""
"""UYGULAMALAR"""

"""
def karesi(x):
    return x**2
8
y = int(input('Lütfen bir sayı giriniz: '))

print(f'Girilen {y} sayısının karesi {karesi(y)}')
"""
"""
x = int(input('Lütfen bir sayı giriniz: '))
y = int(input('Lütfen ikinci sayı giriniz: '))

summation = lambda x, y: x + y
multiply = lambda x, y : x * y 

print(f'Girilen {x} sayısının ve {y} sayısının toplamı {summation(x, y)} çarpımı {multiply(x, y)}')
"""
"""
def multipy(mylist):
    mult = 1
    for x in mylist:
        mult *= x
    return mult 
list1 = [3, 5, 6, 10]
print(multipy(list1))
"""
"""

"""
"""
def cube_c(a):
    return 12*a

def cube_a(a):
    return 6*a**2

def cube_v(a):
    return a**3

a = int(input('Lütfen kenar uzunluğunu giriniz:'))
print(f'Kenatı {a} olan küpün çevresi {cube_c(a)}, alanı {cube_a(a)}, hacmi {cube_v(a)} dir')
"""