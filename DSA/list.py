# list are mutable and in built data structures
# data structure is a way to store and organize data for quikc/easy access

num = [1, "2", [4, 5], 8, 0]
print(num)
print(num[2])
print(num.append(11))
print(num)
print(len(num))
print(num[-1])
del num[2]
print(num)

# tuples
tuple1 = (1, 2, 3, 4)
print(type(tuple1))

# dictionary
dict_name = {'name': 23, 'address': 'Vienna 51', 'visa': {'type': 'schengen', 'country': 'germany'}}
print(dict_name)
dict_name['role'] = 'CTO'
print(dict_name)
print(dict_name['role'])

