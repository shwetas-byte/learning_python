# lambda--a function having no name is called lambda function it is made to use at a time only once 
# by default isme value return hoti hai isme return nahi likhte hai
# x=lambda a,b:a+b
# # x(5,10)
# print(x(5,10))

# x=lambda a:print(a**2)
# a=int(input("Enter value you want to do square:"))
# x(a)

# map+lambda
# l=[1,2,3,4,5]
# print(list(map(lambda a:a**2,l)))

# l=eval(input("Enter any list:"))
# l1=eval(input("Enter any list:"))
# l2=eval(input("Enter any list:"))
# print(list(map(lambda n1,n2,n3:n1+n2+n3,l,l1,l2)))


# lamda with filter
# l1=eval(input("Enter any list:"))
# print(list(filter(lambda n:n%2==0,l1)))
# print(list(filter(lambda n:n if n%2==0 else None,l1)))

# lambda with reduce
# import functools
# from functools import reduce
# l1=eval(input("Enter any list:"))
# print(reduce(lambda a,b: a if a>b else b,l1))

# l1=eval(input("Enter any list:"))
# print(reduce(lambda a,b: a if a<b else b,l1))







