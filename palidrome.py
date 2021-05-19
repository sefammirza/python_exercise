inputvalue = "Ey edip adana'da,   ][] pide ye!".lower()
print('palidrome' if [*filter(lambda x: x.isalpha() , inputvalue)]==[*filter(lambda x: x.isalpha(), reversed(inputvalue))] else 'degil')
# if [*filter(lambda x: x.isalpha() , inputvalue)]==[*filter(lambda x: x.isalpha(), reversed(inputvalue))]:
#     print('palidrome')
# else:
#     print('degil')