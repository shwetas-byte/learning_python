while True:
    print('1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division\n 5.Floor division\n 6.OFF')
    n=int(input("Enter above mention any one option:"))
    num=[1,2,3,4,5,6]
    if n in num:
        if n==1:
            x=int(input('Enter how many you want to add:'))
            l=[]
            sum=0
            for _ in range(1,x+1):
                number=int(input(f'Enter {_} number:'))
                l.append(number)
                sum+=number
            print(f'Addition of given number {l} is {sum}')

        elif n==2:
            x=int(input('Enter how many you want to subtract:'))
            l=[]
            for _ in range(1,x+1):
                number=int(input(f'Enter {_} number:'))
                l.append(number)
                sub=l[0]
                sub-=number
            print(f'Subtraction of given number{l} is {sub}')

        elif n==3:
            x=int(input("Enter how many number you want to multiply:"))
            l=[]
            mul=1
            for i in range(1,x+1):
                number=int(input(f'Enter {i} number:'))
                l.append(number)
                mul*=number
            print(f'Multiplication of {l} is {mul}')

        elif n==4:
            x=int(input("Enter how many number you want to divide:"))
            l=[]
            for i in range(1,x+1):
                number=int(input(f'Enter {i} number:'))
                l.append(number)
                div=l[0]
                div/=number
            print(f'Divide of {l} is {div}')

        elif n==5:
            x=int(input("Enter how many number you want to do floor divide:"))
            l=[]
            for i in range(1,x+1):
                number=int(input(f'Enter {i} number:'))
                l.append(number)
                div=l[0]
                div//=number
            print(f'Divide of {l} is {div}')
        
        else:
            break

    else:
        print('Please enter valid option:')