left = set("qwertasdfgzxcvb")
right = set("yuiophjklmn")
word = set("sefa")

leftcheck = bool(word.intersection(left))
rightcheck = bool(word.intersection(right))

print(leftcheck and rightcheck)
