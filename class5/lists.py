########################     class 4       #################
# print("Hello")
# print("world")
#
# print("Hello")
# print('\n')   #new line
# print("world")
#
# print('c:\docs\naveen')
# #Raw String
# #Raw string is a string that returns it as it is without making any changes to it.
# print(r'c:\docs\naveen')

# Repetition - To print multiple times
#how will you print in next line? Homework
print(3 * 'vivek')


# #ValueError
# name = input("Enter your name")
# print(name) #give integer number and find type of it
# print(type(name))
# name = int(input("Enter a number"))
# print(name) #give integer and string values and show value error
# print(type(name))

# name = 'vivek'
# #print(name1)

# String in python is immutable
# you cannot change string values
# name ='Vivek'
# name[0] = 'R'
# name[1:4] = 'bcd'
#We can’t change the string, because string is immutable
# but we can do concatenation
# print('hi ' + name[1:4])

#List
# collection of values of same or different data type
# numbers = [23, 67, 89, 50]
# print(numbers)
# print(numbers[0])
# numbers[0] =100
# print(numbers)  #numbers = [100,67,89,50]
# #print(numbers[4])  #error index out of range
# print(numbers[1:3]) # [67,89]
# print(numbers[0:]) # [100,67,89,50]
# print(numbers[:2]) # [100,67]
# print(numbers[:]) # [100,67,89,50]
# print(numbers[-1]) # [50]
# print(numbers[-1:-4]) #[50,89,67]
# print(numbers[-1:-5]) # error
#print(numbers[-5])

###########################      Class 5    #########################
# # compare list with array in c. we have to use for loop to print array each array elements.
# # imperative & declarative
# #
# # letters = [10, 20, 30, 40]
# #     index:  0   1   2   3
# #     length: 1   2   3    4
# #
# # list maximum size?

numbers = [100,67,89,50]
print(len(numbers))
#print("length: " + len(numbers))
print("Hello" + 'World')
print('length: ' + str(len(numbers)))
# use of f string
print(f"Address: {id(numbers)}")
print(f"Address: {id(numbers[0])}")
print(f"Address: {id(numbers[1])}")
print(f"Address: {id(numbers[2])}")
print(f"Address: {id(numbers[3])}")

numbers = [100,67,89,50]
names = ['Arun', 'Mary', 'Dora']
print(names)
names[0] = "Peter"
print(names)

#Lists are mutable
# we can change values. we can append() and insert() values
# append(value) adds at the end of the list &
# insert(index,value) adds in a specific place.

# to add a single values to list
names.append("John")
print(names)
names.append(-1)  # u can append numbers(diff data type)
print(names)

# List can hold different datatype values
values = [23, 'Arun', 67.6, 'Mary', 89, 95.6]
print(values)

# Joining two list using + operator
join_list = numbers + names
print(f"join list: {join_list}")
join_list1 = names + numbers
print(f"join list1 {join_list1}")

# Joining two lists using extend()
favorite_numbers = [100, 200, 300, 400]
names = ["selvi","vivek",'lilian']
favorite_numbers.extend(names)
print(f"extend favorite numbers list: {favorite_numbers}")
names.extend(favorite_numbers)
print(f"extend names list : {names}")

# To insert values in the list - index, value
shapes = ['circle',"triangle",'line',"dot"]
shapes.insert(3,'Octagon')
print(shapes)

shapes = ['circle, triangle, line, dot']
print(shapes)
print(shapes[0])
#print(shapes[1])

# remove(item) - remove the item from the list
# pop(index)
shapes = ['circle',"triangle",'line',"dot"]
shapes.remove('line')
shapes.remove('circle')
print(shapes)

shapes.append('Octagon')
shapes.append('Oval')
print(shapes)

shapes.pop()
# shapes.pop()
print(shapes)
shapes.append('zigzag')
print(shapes)
shapes.pop(1)
print(shapes)
shapes.clear()
print(shapes)

shapes = ['circle',"triangle",'line',"dot"]
print(shapes.index("line")) #usecases: student rollno
#print(shapes.index("tilde"))

shapes = ['circle',"triangle",'line',"dot",'line']
print(shapes.count("line"))  #usecases: person same name, help to find
# duplicate values

shapes.sort()
print(shapes)
shapes.reverse()
print(shapes)

fruits = ['strawberry','orange','grapes','apple']
fruits2 = fruits.copy() # extra printouts
#students moves from 2nd to 3rd standard(same details:name,address
# + extra students
print(fruits2)




# compare all the list, string functions with c, c++

#
# #del()


