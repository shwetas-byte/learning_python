# comtinue--skip current iterarion
# break--terminate current loop
# pass--skip current block

# n=10
# i=0
# while i<=10:
    
#     if i==5:
#         i+=1  #ye agr nhi lgate toh infinite loop jayega
#         continue
#     print(i)
#     i+=1

# n=int(input("Enter no. of natural no. you want:"))
# for i in range(1,n+1):
#     if i==5:
#         continue
#     print(i)


# n=int(input("Enter any integer:"))
# i=1
# while i<=n:
#     if i==5:
#         pass
#     else:
#         print(i)
#     i+=1

# n=int(input("Enter any integer:"))
# i=1
# while i<=n:
#     if i==4:
#         break
#     else:
#         print(i)
#     i+=1
# print("Hello")

# n=int(input("Enter any integer:"))
for i in range(1,10):
    if i==8:
        break
    else:
        print(i)
print('hello')