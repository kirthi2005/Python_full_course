

#What is an error? unexpected behavior in a program
# that will completely stop your program from
# running

# types of error
# SyntaxError
# ValueError
# TypeError
# IndexError - index out of range
# ZeroDivisionError

#------------------------Divide by zero------------------------------#
#division = 89/0
#print('Hello')
#--------------------------------------------------------------------#

# How to make program continue to run? using try catch

#------------------------Try Except------------------------------#
# try:
#     division = 89/0
# except:    # too broad exception clause. It will catch all
#     #kind of errors
#     print("Error Message: You cannot divide a number by 0")
# print('Hello')
#----------------------------------------------------------------#

#------------------------Value Error------------------------------#

# number = int(input("Enter a number: "))  # enter string value
# print(number)
# print("Hello")
#------------------------------------------------------------------#

#------------------------Two Error one Except--------------------------#
# try:
#     division = 89/0
#     number = int(input("Enter a number: "))   # enter string value
#     print(number)
# except:    # too broad exception clause. It will catch all
#     #kind of errors
#     print("Invalid Input")
#----------------------------------------------------------------------#

#------------------------Each Error, one Except--------------------------#
# try:
#     division = 89/0
#     number = int(input("Enter a number: "))   # enter string value
#     print(number)
# except ZeroDivisionError:
#     print("Divided by Zero")
# except ValueError:
#     print("invalid input")
# print('hello')
#------------------------------------------------------------------------#

#-----------------------Catch Error in a variable-------------------------#
# try:
#     division = 89/0
#     number = int(input("Enter a number: "))   # enter string value
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print("invalid input")
# print('hello')
#------------------------------------------------------------------------#