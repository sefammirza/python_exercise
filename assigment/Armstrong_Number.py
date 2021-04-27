number = input("Please enter a number: ")
number_list = list(number)
cube = []
if number.isnumeric():
    for i in number_list:
        cube.append(int(i)**len(number))
    if sum(cube) == int(number):
        print("{} is an Armstrong number".format(number))
    else:
        print(" {} is not an Armstrong number".format(number))
else:
    print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")
    
    