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
    
# while i<=n:
#     sum+=i
#     if i<n:
#         print(i,end='+')
#     else:
#         print(i,end='=',)
#     i+=1
# print(sum)


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

n=eval(input("Enter terminating point:"))
mul,i=1,1   
while i<=n:
    mul*=i
    if(i<n-1):
       print(i,end='*') 
    else:
        print(i,end='=')
    i+=2
print(mul)