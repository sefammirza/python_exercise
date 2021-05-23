"""
name = 'arin'
age = 20
 
def hello():
    name = 'mahmut'
    age = 10
    message = f'Benim adım {name} ve {age} yaşındayım'
    print(message)
    
hello()
"""
"""
x = 'global'

def myfunc():
    x = 'local'
    return x

print(x)

print(myfunc())"""

x = 'global level'

def enclosing():
    x = 'enclosing level'
    def innerfunc():
        x = 'local level'
        print(x)
    innerfunc()
    
enclosing()