# two types of function ---
# 1. pre define function
# 2.user defined:

# 2.1 function without return value(no return function):

# 1.without parameter no return-- read only function
# kbhi bhi input nhi lenge iske andr work toh krega but sahi format nahi haii
# syntax---
# def funtion_nmae():
#      //statement
# def show():
#     print('welcome')
# show()
# def rupees():
#     a=10000
#     print("ur balance is",a)
# rupees()


# 2. with parameter no return
# def div(a,b):
#     print(a//b)
# a=int(input("Enter 1 no."))
# b=int(input("Enter 2 no."))
# div(a,b)

# def swapp(a,b):
#     a=a+b
#     b=a-b
#     a=a-b
#     print(f"a after swapping is {a} ")
#     print(f"b after swapping is {b} ")
# swapp(2,3)

# Q1. write a program to display the sum of three digit number uswing function
# ?Note not aloowed more than 3 digit and less than 3 digit no.
# add =0
# def summ(a):
#     add=0
#     if 100<= a <= 999:
#         while a>0:
#             digit=a%10
#             add=add+digit
#             a//=10
#         print(add)
#     else:
#         print("invalid number")
# a=int(input("Enter a 3 digit number:"))
# summ(a)
# Q2.Write a program to print the table of any number using function
# def table(num):
#     for i in range(1,11):
#         print(f"{num} x {i} = {num*i}")
# a=int(input("Enter a  number to print table:"))
# table(a)


# with parameter with return
# q1 wap to print table of any number
# Q2 wap to print the even no.from a list
# def even(li):   
#     for i in li :
#         if i%2==0:
#             print(i)
# size=int(input("Enter size of list:"))
# li=[]
# for i in range(size):
#     v=int(input(f"Enter {i+1} value:"))
#     li.append(v)
# print(li)
# even(li)
# li=eval(input("Enter any list:"))
# print(type(li))
# even(li)

def update(li):
    # li1=[]
    # for i in li:
    #     li1.append(i+10)
    # return li1
    li[i]=li[i]+10
    return li

size=int(input("Enter size of list:"))
li=[]
for i in range(size):
    v=int(input(f"Enter {i+1} value:"))
    li.append(v)
print(li)
print(update(li))




# -----neeraj sir-----
# def add():
#     print('Addition is:',5+6)
# add()  #onlyy display krta hai no return value
# print(add())  #add ki jo by default value hai none vo bhi print hoga with display
# x=add()  #display with return value
# print(x)

# without argument without return
# def fun():
#     print('hello')
# fun()

# def greet():
#     print("Welcome to our webpage")
# greet()


# without argument with return
# def add():
#     return 4+9
# print('Addition is',add())

# def greet():
#     return 'welcome to our webpage'
# print(greet())


# with argument without return
# def add(x,y):
#     print('Addition is:',x+y)
# x=int(input("enter first number:"))
# y=int(input("enter first number:"))
# add(x,y)

# def greet(name):
#     print(f'welcome {name}') 
# name=input("Enter your name:")
# greet(name)


# with return with argument
# def add(x,y):
#     add=x+y
#     return add
# x=int(input("enter first number:"))
# y=int(input("enter first number:"))
# print('Addition is:',add(x,y))


# def greet(name):
#     return f'Welcome {name}'
# name=input("Enter your name:")
# print(greet(name))

# Relation b/w parameter & arguments
# 1.Positional argument
# def show(x,y,z):
#     print('x:',x)
#     print('y:',y)
#     print('z:',z)
# show(10,20,30)
# show()   #show() missing 3 required positional arguments: 'x', 'y', and 'z'---|
# show(10)   #show() missing 2 required positional arguments: 'y' and 'z'       |---- default positional argument
# show(10,20)   #show() missing 1 required positional argument: 'z'-------------|
# show(10,20,30,40)  #show() takes 3 positional arguments but 4 were given------|-----variable length argument


# 2.Default positional argument
# def add(x=0,y=0,z=0):
#     print(x+y+z)
# add()  #0
# add(10) #10
# add(10,20)  #30
# add(10,20,30) #60
# add(10,20,30,40)   #add() takes from 0 to 3 positional arguments but 4 were given


# 3.variable length positional argument  (*args) --hold as an tuple datatype tuple
# * it has packing function in parameter and unpacking in argument
# def display(*args):
#     print(args)
#     print(type(args))
# display()
# display(10,20)
# display(10,'python',[1,3,4,5])

# def display(*n):
#     sum=0
#     for i in n:
#         sum+=i
#     print(sum)
# display(10,20,30,40,50,60)

# def display(*n):
#     sum=0
#     for i in n:
#         sum+=i
#     print('Addition is:',sum)
# values=eval(input("Enter all values:"))
# display(*values)  

# natural no.
# def natural_num(n):
#     for i in range(1,n+1):
#         print(i)
# n=eval(input('enter how many natural no. you want:'))
# natural_num(n)


# 4.Key word argument
# def add(x,y,z):
#     print('x:',x)
#     print('y:',y)
#     print('z:',z)
# add(y=20,x=2,z=100)
# add()  #missing 3 required positional arguments: 'x', 'y', and 'z'     ---|
# add(x=10)  #Vmissing 2 required positional arguments: 'y' and 'z          |---- default key-word argument
# add(x=10,y=20)   #missing 1 required positional argument: 'z'-------------|
# add(x=10,y=20,z=30,t=40)   #got an unexpected keyword argument 't'  ------|-----variable length key-word argument



# 5.default key-word argument
# def add(x=0,y=0,z=0):
#     print('x:',x)
#     print('y:',y)
#     print('z:',z)
# add()
# add(x=10)
# add(x=20,y=30)
# add(x=20,y=30,z=40)


# 6.variable length key-word argument
# def add(**kwargs):
#     print(kwargs)
#     # print(sum)
#     print(type(kwargs))
# add()
# add(x=10,y=20,z=30,r=40)



# def add(**kwargs):
#     sum=0
#     for i in kwargs:
#         sum+=kwargs[i]
#     print(sum)
# di=eval(input("Enter the values for sum:"))
# # add(x=10,y=20,z=30)
# add(**di)


#summary:- def fun_name(positional,default_positional,variable-length positional arg,keyword arg,default key-word,variable length key-word arg)