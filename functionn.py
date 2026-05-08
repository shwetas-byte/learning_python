
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