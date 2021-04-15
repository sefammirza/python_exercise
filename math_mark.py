math_mark = int(input('Please enter the mark: '))
if 100 >=math_mark >= 85:
    print('A(Excellent)')
elif 84 >= math_mark >= 70:
    print('B(Good)')
elif 69 >= math_mark >= 60:
    print('C(Medium)')
elif 59 >= math_mark >= 45:
    print('D(Not Bad)')
elif 44 >= math_mark >= 0:
    print('F(Failed)')
else:
    print('You entered the wrong value.')
    