# if--independent keyword bcz condition true block execute otherwise block doesn't execute

# single-condition question
# 1.no. is even or odd
n=eval(input("Enter any number:"))
if n==0:
    print(f'given number {n} is zero')
elif n<=0:
    print(f'given no. {n} is negative')
elif n%2==0:
    print(f'given no. {n} is even')
elif n%2!=0:
    print(f'given no. {n} is odd')
else:
    print(f'given number {n} is invalid')