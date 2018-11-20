import os
dir()
os.getcwd()
os.chdir('C:\\Venkat\\Personal\\Trainings\\Python')
os.getcwd()

# modules

import modulefun as mf  # modulefun shpuld be available in the above mentioned path
mf.add(2,5,6)
mf.fib(50)
print(mf.a)

from modulefun import add
add(2,5,6)

# Packages

import PYTHON_OCT2018.modulefun as md
md.add(4,5,6)
 