# this lesson will show you how to install and
#uninstall third party external modules

from math import *
print(sqrt(144)) #if it is a large file we don't
# know where sqrt() will come from

import math
print(math.sqrt(16)) # if we import this way we can
# easily tell sqrt function is coming from math module

import useful_tools
print(useful_tools.roll_dice(10))

from useful_tools import *
print(roll_dice(10))

# u can find a list of modules in below link
# https://docs.python.org/3/py-modindex.html

# two types of modules - Built in Modules (built into
# the Python language. we automatically access to
# them and External Modules

# In the folder structure on left - External libraries
# - Lib - external modules will present
# some built in modules available at
# C:\Users\<YourName>\AppData\Local\Programs\Python\Python3x\Lib

#math.py built in not available in above link
#The math module is a built-in C extension module, not a regular .py file written in Python.
#That means it’s written in C and compiled,
# so it runs super fast — especially important for
# mathematical operations. It's part of Python's core,
# so it's compiled into the interpreter or stored as
# a .pyd (Windows) or .so (Unix) file.

# for third party modules you have to install them
# search in google for python-docx
# https://python-docx.readthedocs.io/en/latest/
# https://python-docx.readthedocs.io/en/latest/user/install.html

#pip is a command to install python modules. It's
#referred to as package manager. Package manager
# allows you to install, manage, update and uninstall
# different python modules.Pip is preinstalled after
# version 3.
#
# To check pip version
#   pip --version

# pip install python-docx -> will install everything we
#need for python-docx
#pip install --upgrade pip
# where you can see python-docx?
#External Libraries - Lib - site-packages - u can see
# docx
# pip show python-docx
#pip uninstall python-docx
#pip install python-docx
# pip list
#py -3.13 -m pip install --upgrade pip
#py -3.13 -m pip install python-docx

'''
You had Python 3.13 installed via Microsoft Store ✅

python-docx was installed, but not in the right place initially ❌

After using py -3.13 -m pip install python-docx it got installed for the correct Python version ✅

Now the import works perfectly 🎯
'''


#import docx

#print(dir(docx))

# u can access methods in docx using docx.

# to uninstall pip uninstall python-docx


