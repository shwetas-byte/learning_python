
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
def show(x,y,z):
    print('x:',x)
    print('y:',y)
    print('z:',z)
# show(10,20,30)
# show()   #show() missing 3 required positional arguments: 'x', 'y', and 'z'---|
# show(10)   #show() missing 2 required positional arguments: 'y' and 'z'       |---- default positional argument
# show(10,20)   #show() missing 1 required positional argument: 'z'-------------|
# show(10,20,30,40)  #show() takes 3 positional arguments but 4 were given------|-----variable length




# 2.Default positional argument