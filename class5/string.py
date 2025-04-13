#get marks from user and print the total

#variable with string - f string, + , { }
# print -> Hello Vivek! You are 18 years old. You got cash price of $999.99

name = 'Vivek'
print('Hi {name}')
print(f'Hi {name}')

name = "KIRUTHIKA"
print(name.isupper())
print(name.islower())
print(name.isdecimal())

word = "Women Empowerment"
print(word.upper().isupper())
print(word.index("w"))
print(word.index("erme"))

print(word.find("w"))
print(word.find("erme"))

print(word.index("z")) # error
print(word.find("z"))  # find

print( 5 * 6 + 11)
print( 5 * (6 + 11))
print( 13 % 5) #3
print ( 13 // 5) #2

my_number = -101
print(abs(my_number))
print(pow(2,4)) #2^4 = 2*2*2*2
print(max(250,3000))
print(min(250,3000))
print(round(6.4))
print(round(6.5)) #6
print(round(6.6))
print(round(6.9)) #7

#math - module
from math import *
print(round(3.7))
print(floor(3.7)) # 3
print(round(3.2))
print(ceil(3.2)) # 4
print(sqrt(121)) # 11

