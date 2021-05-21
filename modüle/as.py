from upper_packege import my_packege1, my_packege2
from upper_packege.my_packege1 import my_module_1,my_module_2
from upper_packege.my_packege2 import my_module_3, my_module_4

print(my_module_2.divide(10, 5))
print(my_module_1.addition(4, 5))
print(my_module_3.repeater("clarusway", 4))
print(my_module_4.sqroot(25))
print(my_module_1.__spec__)

import upper_packege
print(dir(upper_packege))

from upper_packege.my_packege1.my_module_2 import divide,hello

hello()
print(divide(22, 11))

import math
from math import log10
print(log10(1000))
print(math.__doc__)
print(my_module_2.__doc__)


