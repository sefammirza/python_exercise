name = "Joseph"
password = " W@12"

enter = input("Please enter name: ")

if name == enter:
    print("Hello, {}! The password is : {}".format(name, password))
else:
    print("Hello, {}! See you later.".format(enter))