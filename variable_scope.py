# variable scope
# 1.local scope
# 2.global scope
# 3.non-local scope

# def add():
#     x=10
#     print(x)
# add()
# print(x)   #error ayegabcz ye local me define hai



# x=20
# def add():
#     print(x)   #error dega kyuki local ki priority jyada hoti h
#     x=10
#     print(x)
# add()
# print(x)


# accessing local variable in global
# def add():
#     global x  #local variable ko global me use krne ke liye global keyword use krte hai
#     x=10
#     print(x)
# add()
# print(x)



# condition if global and local has same name toh global ki value local me kaise access kre----we use globals method
# accessing global variable in local
# x=10
# def add():
#     x=50
#     print(x)
#     print(globals()['x'])
# add()
 


 

# if,elif,else,try,except,while,for -- do not create any scope
# function,class -- create newscope
a=int(input("Enter any nymber:"))

if a>0:
    x=10
    # print(x)
elif a<0 :
    x=20
    # print(y)
else:
    x=40
print(x)


