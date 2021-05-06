def absolute(num) :
    """
This function returns the absolute
value of the entered number
    """
    if num >= 0 :
        return num
    else:
        return -num
print(absolute.__doc__)
print(absolute(-11))
print(absolute(50))