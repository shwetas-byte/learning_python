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

# without argument with return
# def add():
#     return 4+9
# print('Addition is',add())

# with argument without return
# def add(x,y):
#     print('Addition is:',x+y)

# x=int(input("enter first number:"))
# y=int(input("enter first number:"))
# add(x,y)

# with return with argument
def add(x,y):
    add=x+y
    return add
x=int(input("enter first number:"))
y=int(input("enter first number:"))
print('Addition is:',add(x,y))


