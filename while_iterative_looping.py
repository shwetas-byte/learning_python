# iterative--to avoid repetition of code for continupus program we use iterative statement
# while--infinite iteration
# for--finite iteration,,collection data type
# while syntax:
#1. while condition:
    # while body

# 2.startpoint
# while terminatin_point:
    # while body
    # incre/decre---responsible for finite loop
# condition always n+1 check hogi and loop hmesa n times chlega

# while True:
#     print("Hello")

# n=eval(input("Enter no. of terms you want:"))
# i=1
# sum=0
# while i<=n:
#     # print(i)
#     print(i,end=' ')  # linear me lane ke liye
#     i+=1
    
# while i<=n: 
#     if i<n:
#         print(i,end=',')
#     else:
#         print(i)
#     i+=1
    
# while i<=n:
#     if i<n:
#         print(i,end='+')
#     else:
#         print(i)
#     i+=1
    
# while i<=n:
#     if i<n:
#         print(i,end='+')
#     else:
#         print(i,end='=')
#     i+=1
    


# n=eval(input("Enter terminating point:"))
# mul,i=1,1
# while i<=n:
#     mul*=i
#     if i<n:
#         print(i,end='*')
#     else:
#         print(i,end='=',)
#     i+=1
# print(mul)

# n=eval(input("Enter terminating point:"))
# i=1
# while i<=n:
#     if(i<n):
#         if(i%2==0):
#             print(i,end=',')
#     else:
#         if(i%2==0):
#             print(i)
#     i+=1

# n=eval(input("Enter terminating point:"))
# sum,i=0,2   
# while i<=n:
#     sum+=i
#     if(i<n):
#        print(i,end='+') 
#     else:
#         print(i,end='=')
#     i+=2
# print(sum)

# n=eval(input("Enter terminating point:"))
# mul,i=1,2
# while i<=n:
#     mul*=i
#     if(i<n):
#         print(i,end='*')
#     else:
#         print(i,end='=')
#     i+=2
# print(mul)



# n=eval(input("Enter terminating point:"))
# sum,i=0,1   
# while i<=n:
#     sum+=i
#     if(i<n-1):
#        print(i,end='+') 
#     else:
#         print(i,end='=')
#     i+=2
# print(sum)

# n=eval(input("Enter terminating point:"))
# mul,i=1,1   
# while i<=n:
#     mul*=i
#     if(i<n-1):
#        print(i,end='*') 
#     else:
#         print(i,end='=')
#     i+=2
# print(mul)

# Armstrong no.
# num=eval(input("Enter any number:"))
# temp,original,td,sum=num,num,0,0
# while num>0:
#     td+=1
#     num=num//10
# while temp>0:
#     ld=temp%10
#     sum+=ld**td
#     temp=temp//10
# if(original==sum):
#     print(f'{original} is a armstrong number')
# else:
#     print(f'{original} is not a armstrong number')

# pallindron no.
# for string
# n=input("Enter any string:")
# if n==n[::-1]:
#     print("Pallindrone")
# else:
#     print("not a pallindrome")


# n=eval(input("Enter any  number:"))
# rev,x=0,n
# while n>0:
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# if x==rev:
#     print("Pallindrone")
# else:
#     print("not a pallindrone")

# pattern
# *****
# *****
# *****
# *****
# *****
# n=int(input("Enter any number:"))
# i=1
# while i<=n:
#     print('*'*n)
#     i+=1


# *
# **
# ***
# ****
# *****
# n=int(input("Enter any number:"))
# i=1
# while i<=n:
#     print('*'*i+''*(n-i))
#     i+=1


# *****
# **** 
# ***  
# **   
# *  
# n=int(input("Enter any number:"))
# i=0
# while i<n:
#     print('*'*(n-i)+' '*i)
#     i+=1

# *    
# **   
# ***  
# **** 
# *****
# **** 
# ***  
# **   
# * 
# n=int(input("Enter any number:"))
# i=1
# while i<=n:
#     print('*'*i+' '*(n-i))
#     i+=1
# i=i-2
# while i>0:
#     print('*'*i+' '*(n-i))
#     i-=1


#     *
#    **
#   ***
#  ****
# *****
# n=int(input("Enter any number:"))
# i=1
# while i<=n:
#     print(' '*(n-i)+'*'*i)
#     i+=1


# *****
#  ****
#   ***
#    **
#     *
# n=int(input("Enter any number:"))
# i=0
# while i<n:
#     print(' '*i+'*'*(n-i))
#     i+=1



#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *
# n=int(input("Enter any number:"))
# i=1
# while i<=n:
#     print(' '*(n-i)+'*'*i)
#     i+=1
# i=i-2
# while i>0:
#     print(' '*(n-i)+'*'*i)
#     i-=1

#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# n=int(input("Enter any number:"))
# i=1
# while i<=n:
#     print(' '*(n-i)+'* '*i)
#     i+=1


#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
# n=int(input("Enter any number:"))
# i=0
# while i<n:
#     print(' '*i+' *'*(n-i))
    # i+=1


#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
# n=int(input("Enter any number:"))
# i=1
# while i<=n:
#     print(' '*(n-i)+' *'*i)
#     i+=1
# i=i-2
# while i>0:
#     print(' '*(n-i)+' *'*i)
#     i-=1
