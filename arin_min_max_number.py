minNum = int(input('Please min number: '))
maxNum = int(input('Please max number: '))

for evenNum in range(minNum, maxNum):
    if evenNum % 2 != 0:
        continue
    else:
        print(evenNum)