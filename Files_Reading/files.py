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

# checking file is readable
# print(welcome_message.readable()) # return boolean true or false

# Reading a full file content
# print(welcome_message.read()) # compare with c. while loop EOF condition

# Reading line by line
# print(welcome_message.readline()) # read first line and moving cursor to
# # #next line
# print(welcome_message.readline()) # read 2nd line and moving cursor to
# # #next line
# print(welcome_message.readline()) # read 3nd line and moving cursor to
# # #next line

# Print lines in array/list format
# readlines() is a method used on a file object to read all
# lines from a file and return them as a list of strings.
#Each element in the list represents one line in the file,
# including the newline character \n at the end (unless it's the
# last line and there's no newline).
#.readlines() reads the entire file at once, so avoid using it on
# very large files.
#It returns a list of strings.
#To remove the \n from each line, you can use .strip() or a list
# comprehension:
# print(welcome_message.readlines())

# readlines()[1] right after readlines()[0]?
#print("first line: " + welcome_message.readlines()[0])
#print("second line: " + welcome_message.readlines()[1])

'''
The first call to readlines() reads all the lines and moves the file 
pointer to the end of the file.So when you call readlines() again on 
the second line, the file is already at the end — there’s nothing 
left to read, hence the IndexError.
1. The first f.readlines() already reads the entire file and moves 
the pointer to the end.
2. So the second call to readlines() returns an empty list.
3. You'll get: IndexError: list index out of range
'''

# strip() for \n

# lines = welcome_message.readlines()
# print(lines[0].strip())  # Line 0
# print(lines[1].strip())  # Line 1
# print(lines[2].strip())  # Line 1

# using FOR Loop
for message in welcome_message:
    print(message)


welcome_message.close()  # like fclose() in c

# show him file not found error






