numbers =[1, 3, 7, 4, 3, 0, 3, 6, 3]
again = max(numbers, key=numbers.count)
escape = numbers.count(again)
print("the most frequent number is {} and it was {} times repeated".format(again, escape))
