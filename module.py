#1.inbuilt function
#e.g int(), str()
#2. module
#related function and variables are kept in a file.
#3.user defined functions

import math #import math
print(dir(math))#all function in module math

from math import sqrt   #import specific function
print(sqrt(4))

from math import * #import all modules from math

#3
def func_name(parameter):
    print(parameter)

func_name(10)

def func_name(parameter = 3):
    print(parameter)

func_name()