#Reading files that are outside the python file
# like TEXT file or CSV or HTML

#read command - allow to read  a file that is stored outside of your
#python file.

# filepath - absolute, relative or file name
# mode - r for read,
#        w for write and
#        a for append
#        r+ both read and write

welcome_message = open("hello.txt","r")  #like fopen() in c
# print(welcome_message.readable()) # return boolean true or false
# print(welcome_message.read()) # compare with c. while loop EOF condition

# print(welcome_message.readline()) # read first line and moving cursor to
# #next line
# print(welcome_message.readline()) # read 2nd line and moving cursor to
# #next line
# print(welcome_message.readline()) # read 3nd line and moving cursor to
# #next line

# print(welcome_message.readlines()) # List format example to do list
# welcome_message.seek(0)
# print("first line: " + welcome_message.readlines()[0])
# welcome_message.seek(0)
# print("second line: " + welcome_message.readlines()[1])

# using FOR Loop



welcome_message.close()  # like fclose() in c

# show him file not found error






