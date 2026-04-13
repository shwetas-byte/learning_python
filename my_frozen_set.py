# immutable in nature only difference between set and frozen_set

# s={1,1,2,32,'python','java','php'}
# fs=frozenset(s)
# print (fs)
# print(type(fs))
# print(id(fs))
# print(len(fs))
# print(max(fs))
# print(min(fs))
# print(sum(fs))


# 1.union()
# s={1,1,'python','java','php'}
# fs=frozenset(s)
# s1={'shweta','riya','yash','pihu','java'}
# fs1=frozenset(s1)
# print(fs.union(fs1))

# 2.intersection
# s={1,1,'python','java','php'}
# fs=frozenset(s)
# s1={'shweta','riya','yash','pihu','java'}
# fs1=frozenset(s1)
# print(fs.intersection(fs1))

# 3.difference()
# s={1,1,'python','java','php'}
# fs=frozenset(s)
# s1={'shweta','riya','yash','pihu','java'}
# fs1=frozenset(s1)
# print(fs.difference(fs1))

# 4.symmetric_difference()
s={1,1,'python','java','php'}
fs=frozenset(s)
s1={'shweta','riya','yash','pihu','java'}
fs1=frozenset(s1)
print(fs.symmetric_difference(fs1))
