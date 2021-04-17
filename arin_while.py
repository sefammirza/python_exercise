
number = 1

while number <= 10:
    print(number)
    number = number + 1
    """


message = ''
while message != 'quit':
    message = input('quit yazana kadar bu mesajı göreceksinsad')
    print(message)
    """
"""
my_flag = True
message = ''

while my_flag:
    message = input('Çıkmak için quit yazınız:')
    if message == 'quit ':
        my_flag = False
    else:
        print(message)
        """

"""
number = 1

while number < 10 :
    print(number)
    if number == 5:
        break
    number += 1
    """

number = 1

while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(number)