def parrot_trouble(talking,hour):
    if 6 <= hour <= 21 or talking == False:
        return False
    elif (talking == True) and 23 >= hour >= 21 or hour <= 6:
        return True
print(parrot_trouble(True, 5))
print(parrot_trouble(True, 8))
print(parrot_trouble(False, 22))