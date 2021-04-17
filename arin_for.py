celciuses = [20, 25, 30, 35]
kelvin = []
fahrenheit = []

for c in celciuses:
    k = c + 273
    kelvin.append(k)
    f = c * 9 / 5 + 32
    fahrenheit.append(f)
    
print(kelvin)
print(fahrenheit)