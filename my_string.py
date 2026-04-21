# # character to ascci:ord()
# # ascci to character:chr()
# s=input("Enter any character:")
# x=ord(s)
# # print(x)
# y=x+2
# # print(y)
# print(chr(y))

# print(chr(ord(input("Enter any character:"))+2))

# s=input("Enter your name:")
# print(s)
# print(f'Type of {s} is {type(s)}')
# print(f'ID of {s} is {id(s)}')
# print(f'Max of {s} is {max(s)}')
# print(f'Min of {s} is {min(s)}')
# print(f'Length of {s} is {len(s)}')


# String Methods
# s=input("Enter your name:")
# print(f'Lower of {s} is {s.lower()}')

# s=input("Enter your name:")
# print(f'Upper of {s} is {s.upper()}')

# s=input("Enter your name:")
# print(f'Title of {s} is {s.title()}')

# s=input("Enter your name:")
# print(f'Swap of {s} is {s.swapcase()}')

# s=input("Enter your name:")
# print(f'Capitalize of {s} is {s.capitalize()}')

# s=input("Enter your name:")
# ch=input("Enter any character:")
# start=int(input("Enter start point:"))
# stop=int(input("Enter stop point:"))
# print(f'Index of elementm {ch} in {s} is {s.index(ch,start,stop)}')
# print(input("Enter your name:").index(input("Enter any character:"),int(input("Enter start point:")),int(input("Enter stop point:"))))

# s=input("Enter your name:")
# ch=input("Enter any character:")
# print(input("Enter your name:").count(input("Enter any character:")))


# s="This is python class"
# print(s.split())
# print(s.split('p'))
# print(s.split(' ',2))
# print(s.split(' ',0))
# print(input("Enter any string:").split(input("Enter start point:"),int(input("Enter no. of times you want to split:"))))


# s1='Python'
# s2='Java'
# s3='PHP'
# # x=','.join(s1,s2,s3)    error ayega kyuki join me ek hi argument de skte haii
# x='+'.join([s1,s2,s3])    #list me dena pdega isliye
# print(x,type(x))

# s='!!!Python!!!'
# print(s.strip('!'))
# print(s.lstrip('!'))
# print(s.rstrip('!'))


# s="Learning Python"
# print(s.startswith('Lear'))


# s="Learning Python"
# print(s.endswith('on'))



# print(input("Enter any string:").isalnum())
# print(input("Enter any string:").isalpha())
# print(input("Enter any string:").isascii())
# print(input("Enter any string:").isdecimal())