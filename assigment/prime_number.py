while True:
    value = input('Please enter number: ')
    if not(value.isnumeric()):
        print("You entered wrong")
    else:
        break
if int(value) == 2:
    print("This is a prime number.")
else:
    for i in range(2, int(value)):
        if (int(value) %i) == 0:
            print("This is not a prime number.")
            break
    else:
        print("This is the prime number.")