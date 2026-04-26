# character to ascci:ord()
# ascci to character:chr()
# s=input("Enter any character:")
# x=ord(s)
# print(x)
# y=x+2
# print(y)
# print(chr(y))

# s=input("Enter any string:")
# s=''
# for ch in s:
    # print(chr(ord(ch)+1))
#     s1=s1+chr(ord(ch)+1)
# print(s1)

# l=eval(input("Enter any list:"))
# l1=[]
# for i in l:
#     l1.append(i+5)
# print(l1)

# l=eval(input("Enter any lsit:"))
# l1=[]
# for i in l:
#     l1.append(i**2)
# print(l1)

# t=eval(input("Enter any tuple:"))
# l=list(t)
# l1=[]
# for i in l:
#     l1.append(i+5)
# t=tuple(l1)
# print(t)

# l=eval(input("Enter any list:"))
# for i in range(len(l)):
#     # x=l[i]+5
#     l[i]=l[i]+5
# print(l)

# d=eval(input("Enter any dictionary:"))
# for i in d:
    # print(i)
    # print(i,'=',d[i])

# d=eval(input("Enter any dictionary:"))
# for i in d.keys():
#     print(i)

# for i in d.values():
#     print(i)

# for i,j in d.items():
#     print(i,'=',j)

# for i in d:
#     print(d[i])


# s={10,20,30,30}
# for i in s:
#     print(i)

# n=int(input("enter any number:"))
# for i in range(1,n+1):
    # print('*'*i+''*(n-i))
    # print(' '*(n-i)+'*'*i)
    # print(' '*(n-i)+'* '*i)


# n=int(input("Enter any number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end=' ')
#     print()


# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# n=int(input("Enter any number:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15
# n=int(input("Enter any integer:"))
# x=1
# for _ in range(1,n+1):
#     for j in range(1,_+1):
#         print(x,end=' ')
#         x=x+1
#     print()


# 2 
# 4 6 
# 8 10 12 
# 14 16 18 20 
# 22 24 26 28 30 
# n=int(input("Enter any integer:"))
# x=2
# for i in range(1,n+1):
#     for _ in range(1,i+1):
#         print(x,end=' ')
#         x=x+2
#     print()

# 1 
# 3 5 
# 7 9 11 
# 13 15 17 19 
# 21 23 25 27 29 
# n=int(input("Enter any integer:"))
# x=1
# for i in range(1,n+1):
#     for _ in range(1,i+1):
#         print(x,end=' ')
#         x=x+2
#     print()


# A 
# A B 
# A B C 
# A B C D 
# A B C D E 
# n=int(input("Enter any integer:"))
# for i in range(1,n+1):
#     x='A'
#     for _ in range(1,i+1):
#         print(x,end=' ')
#         x=chr(ord(x)+1)
#     print()


# A 
# B C 
# D E F 
# G H I J 
# K L M N O 
# n=int(input("Enter any integer:"))
# x='A'
# for i in range(1,n+1):
#     for _ in range(1,i+1):
#         print(x,end=' ')
#         x=chr(ord(x)+1)       
#     print()



#     A
#    CB
#   FED
#  JIHG
# ONMLK
# n = int(input("Enter no. of rows you want: "))
# x = 'A'
# for i in range(1, n + 1):
#     row = ''
    
#     for _ in range(i):
#         row = x + row
#         x = chr(ord(x) + 1)
    
#     print(' ' * (n - i) + row)


n=int(in)