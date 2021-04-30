while True:
    value = input('Please enter number: ')
    if not(value.isnumeric()):
        print("You entered wrong")
    else:
        break
if int(value) == 2:
    print("bu bir asal sayidir")
else:
    for i in range(2, int(value)):
        if (int(value) %i) == 0:
            print("asal sayi DEGILDIR")
            break
    else:
        print("asal sayidir")