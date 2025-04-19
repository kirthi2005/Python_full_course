# # Dictionary uses { } .
# #It has key value pairs.
# # ( like normal dictionary has its word & its explanation )
#
data = {"name":"Vivek","rno":11,"sec":"b"}
# print(data['rno'])
#
# #
# print(data['name'])
# # print(data['unknown'])
#
# print(data.get('name'))
# #
# data_dic = {1:"abc",2:23.3,3:'ghi'}
# print(data_dic[2])


# # # List to Tuple
# my_list = [1, 2, 3]
# tuple_version = tuple(my_list)
# print(tuple_version)
# #
# # # Tuple to List
# my_tuple = (1, 2, 3)
# list_version = list(my_tuple)
# print(list_version)
#
# # # List to Set (removes duplicates)
# my_list = [1, 23,45,2, 2, 3]
# set_version = set(my_list)  # {1, 2, 3}
# print(set_version)
# #
# # # Set to List
# my_set = {1, 2,3}
# list_version = list(my_set)  # [1, 2, 3] — unordered
# print(list_version)

# Tuple to Set
# my_tuple = (1, 2, 2, 3)
# print(my_tuple)
# set_version = set(my_tuple)  # {1, 2, 3}
# print(set_version)
# # Set to Tuple
# my_set = {1, 2, 3}
# tuple_version = tuple(my_set)  # (1, 2, 3) — unordered
# print(my_set)

# Invalid
# print(dict({1, 2, 3}) ) # Error

# Valid (list of pairs)
# dict_valid = dict([('x', 100), ('y', 200)])
# print(dict_valid)

#Dict → List / Tuple / Set
# by default it takes only keys
# my_dict = {'a': 1, 'b': 2}
# #
# list_keys = list(my_dict)      # ['a', 'b']
# tuple_keys = tuple(my_dict)    # ('a', 'b')
# set_keys = set(my_dict)        # {'a', 'b'}
# print(list_keys,tuple_keys,set_keys)
# print(str(list_keys)+ "\n" +str(tuple_keys) + "\n" + str(set_keys))
#
# # list_of_pairs = [('a', 1), ('b', 2)]
# # dict_version = dict(list_of_pairs)  # {'a': 1, 'b': 2}
# # print(dict_version)
#
# my_dict = {'a': 1, 'b': 2}
# # Values as a list
# list_values = list(my_dict.values())    # [1, 2]
# # Values as a set
# set_values = set(my_dict.values())      # {1, 2}
# # Values as a tuple
# tuple_values = tuple(my_dict.values())  # (1, 2)
# print(list_values)
# print(set_values)
# print(tuple_values)
#
# my_dict = {'name': 'vivek', 'rollno': 12}
# # Keys
# list_keys = list(my_dict.keys())        # ['a', 'b']
# list_keys1 = list(my_dict.values())
# # Items (key-value pairs)
# list_items = list(my_dict.items())      # [('a', 1), ('b', 2)]
# print(list_keys)
# print(list_keys1)
# print(list_items)

# keys = ['name','age','rno']
# values = ['Arun',28,12]
# data_list_dic = dict(keys)

# The zip() function combines multiple iterables (like lists, tuples,
# etc.) element-wise into tuples, pairing elements by their index.

#
keys = ['name','age','rno']
values = ['Arun',28,12]
data_list_dic = zip((keys, values))
print(data_list_dic)
data_list_dic= dict(zip(keys, values))
print(data_list_dic)
# print(zip(keys, values))
print(list(zip(keys, values)))
print(set(zip(keys,values)))
print(tuple(zip(keys,values)))
