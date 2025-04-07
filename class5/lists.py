print("Hello")
print("world")

print("Hello")
print('\n')   #new line
print("world")

print('c:\docs\naveen')
#Raw String
#Raw string is a string that returns it as it is without making any changes to it.
print(r'c:\docs\naveen')

# Repetition - To print multiple times
#how will you print in next line? Homework
print(3 * 'vivek')


#ValueError
name = input("Enter your name")
print(name) #give integer number and find type of it
print(type(name))
name = int(input("Enter a number"))
print(name) #give integer and string values and show value error
print(type(name))

name = 'vivek'
#print(name1)

# String in python is immutable
# you cannot change string values
# name ='Vivek'
# name[0] = 'R'
# name[1:4] = 'bcd'
#We can’t change the string, because string is immutable
# but we can do concatenation
print('hi ' + name[1:4])

#List
# collection of values of same or different data type
numbers = [23, 67, 89, 50]
print(numbers)
print(numbers[0])
numbers[0] =100
print(numbers)  #numbers = [100,67,8950,]
#print(numbers[4])  #error index out of range
print(numbers[1:3]) # [67,89]
print(numbers[0:]) # [100,67,89,50]
print(numbers[:2]) # [100,67]
print(numbers[:]) # [100,67,89,50]
print(numbers[-1]) # [50]
print(numbers[-1:-4]) #[50,89,67]
print(numbers[-1:-5]) # error
print(numbers[-5])

print(len(numbers))
#print("length: " + len(numbers))
print("Hello" + 'World')
print('length: ' + str(len(numbers)))


'''names = ['Arun', 'Mary', 'Dora']
print(names)

values = [23, 'Arun', 67.6, 'Mary', 89, 95.6]
print(values)

join_list = numbers + names
print(join_list)
join_list = names + numbers
print(join_list)

# functions or methods on list
#values.

#Lists are mutable
# we can change values. we can append() and insert() values
# append(value) adds at the end of the list &
# insert(index,value) adds in a specific place.

print(names)
names.append('Barbie')
print(names)

print(numbers)
numbers.insert(4,500)
print(numbers)
numbers.append(-1)
print(numbers)

# remove(item) - remove the item from the list
# pop(index)
#numbers.remove(6)
numbers.remove(500)
print(numbers)
numbers.pop()
print(numbers)
numbers.pop(1)
print(numbers)

#del()
#extend()
#min(), max(),sum()
#sort()'''




















