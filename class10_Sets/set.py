# Sets are collection of unique values
# Sets uses { } for indication.
# Set never follows the sequence ie. # Order of values differs

# Sets are like lists - mutable. We can change the
# content inside sets.
# But sets wont allow duplicate values.
# Wont follow sequence (re arrange its position)

# When we print the set, then the sequence of values in output will
# be different from the sequence of input.
int_set = {22,173,12,2,90,22,22}
# print(int_set)
# int_set[0] = 1234
#
# list_set = [22,173,12,2,90,22,22]
# print(list_set)
#Duplicate values present in a set will be printed only once
# in an output.
# int_set = {22,173,12,2,90,22,4,22}
# print(int_set)

# Speed important than its Sequence
#We can’t be sure with the sequence in Set because
# Set uses the concept of hash and using hash we improve the
# performance we want to fetch the element as fast as possible

# Indexing is not supported in sets as it does not follow sequencing.
# so Values can not be changed in a set also because index value
# is not supported.
# print(int_set[2])  # does not support indexing
# int_set[2]=1234
# print(int_set)

print(len(int_set))
int_set.add(23)
print(int_set)

int_set.pop()
print(int_set)
int_set.pop()
print(int_set)

int_set.remove(173)
print(int_set)

