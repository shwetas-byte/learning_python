# map() --create objects
# l1=[1,2,3,4]
# l2=[5,6,7,8]
# l3=[1,2,3,4]
# def sum(n1,n2,n3):
#     return n1+n2+n3
# # res=map(sum,l1,l2,l3)
# # print(res)   #returns only memory address
# res=list(map(sum,l1,l2,l3))
# print(res)
# print(list(res))

# l=[1,2,3,4,5,6]
# def even_odd(n):
#     if n%2==0:
#         return 'even'
#     else:
#         return 'odd'
# res=list(map(even_odd,l))
# print(res)


# filter()--return object
# l=[1,2,3,4,5,6,7,8]
# def even(n):
#     if n%2==0:
#         return n
# res=tuple(filter(even,l))
# print(res)


# l=[1,2,3,4,5,6,7,8]
# def odd(n):
#     if n%2!=0:
#         return n
# res=tuple(filter(odd,l))
# print(res)

import functools
# l=[1,2,3,4,5]
# def add(sum,a):
#     return sum+a
# # print(functools.reduce(add,l))    #isme ye first time me do value uthayega because default value nahi di hai
# print(functools.reduce(add,l,0))

# max value
# l=[10,5,20,30,15,12]
# def max(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# print(functools.reduce(max,l))

# min value
# l=[10,5,20,30,15,12]
# def min(a,b):
#     if a<b:
#         return a
#     else:
#         return b
# print(functools.reduce(min,l))

