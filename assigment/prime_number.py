while True:
    value = input('Please enter number: ')
    if not(value.isnumeric()):
        print("You entered wrong")
    else:
        break
if int(value) == 2:
    print("2 is a prime number.")
else:
    for i in range(2, int(value)):
        if (int(value) %i) == 0:
            print("{}  is not a prime number.".format(value))
            break
    else:
        print("{} is the prime number.".format(value))