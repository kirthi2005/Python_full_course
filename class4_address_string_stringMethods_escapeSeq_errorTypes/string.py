#print()
#input()
# int(), float(), str
# type()
# id() - to get memory address
# hex() - to convert a value to hex value
name ="Programming"
print(name)
print(id(name))
print(hex(id(name)))



#len()
#To find the length of the string
name ="Programming"
print(len(name))
print('length of the value in name variable is: ' + str(len(name)))
#print('length of the value in name variable is: ' + (len(name)))

#To access specific element in a string
name ="Programming"
print(name[0])
print(name[5])
print(name[-1])
print(name[-11])
print(name[0:5])
print(name[0:])
print(name[:5])
print(name[:])

#print(name[11])
#print(name[-12])

#Escape sequences
# \"
#\'
#\\
#\n
print('''  Hi
               Good Morning! 
               How are you
           Thanks & Regards,
           Selvi
        ''')

#statement = 'My dog's name is Daisy'  #error
#print(statement)
statement = "My dog's name is Daisy"
print('statement: ' + statement)

statement1 = 'My dog\'s name Daisy'
print('statement1: '+ statement1)

#statement3 = "My dog"s name Daisy"

statement4 = 'My dog"s name Daisy'
print('statement4: ' + statement4)
statement5 = "My dog\"s name Daisy"
print('statement5: ' + statement5)

#Formatted string f or F
string1 = "Hello"
string2 = "world"
print(f"{string1} {string2} {5+6}")

#String functions
# python everything is an object. dot notation to access
#the method

name ="programmming in python"
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())
name_space ="  Programming in python   "
print(name_space)
print(name_space.strip())#remove white space beginning & end
print(name_space.lstrip())
print(name_space.rstrip())
name_space ="  Programming in python   "
print(name_space.find("gra")) #return index
#python is case sensitive language
print(name_space.find("Gra"))
print(name_space.replace("m","p",-1))
print("in" in name_space) # return boolean
print("hello" not in name_space)
print("hello" in name_space)

# Python is case sensitive

myname='HI'
print(id(myname))
myName = 'hi'
print(id(myName))

myname = 'hi'
print(id(myname))
myName = 'hi'
print(id(myName))

myname = 'hi'
print(id(myname))
myName = 'hello'
print(id(myName))











