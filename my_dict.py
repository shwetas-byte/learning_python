# d={
#     'name':'shweta',
#     '1':'102',
#     'age':37,
#     'qualification':'M.tech'

# }
# d1={
#     2:'shweta',
#     1:'102',
#     3:37,
#     4:'M.tech'

# }
# print(d)
# print(type(d))
# print(len(d))
# print(max(d))
# print(min(d))


# print(d1)
# print(type(d1))
# print(len(d1))
# print(max(d1))
# print(min(d1))
# print(sum(d1))


# Dictionary methods:
# 1.copy()---create new object
# d=eval(input("Enter any dict:"))
# d1=d.copy()
# print(d)
# print(d1)
# print(id(d),id(d1))

# 2.clear()---remove all pairs from dict
# d=eval(input("Enter any dict:"))
# d.clear()
# print(d)
# del d
# print(d)


# 3.get()--d.get(key)-->output value
# d=eval(input("Enter any dict:"))
# x=d.get(input("Enter the key you want to get value of:"))
# print(x)


# 4.keys()--return all keys
# d=eval(input("Enter any dict:"))
# print(d.keys())


# 5.values()---return all values
# d=eval(input("Enter any dict:"))
# print(d.values())


# 6.items()--return key value 
d=eval(input("Enter any dict:"))
print(d.items())

# 7.fromkeys()
# 8.update()
# 9.setdefault()