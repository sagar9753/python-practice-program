# Functions for operation
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def modulo(a,b):
    return a%b
def square(a):
    return a*a
def cube(a):
    return a*a*a
def squ_root(a):
    return a**0.5

def check(a):
    if(a != 'int' and a != 'float'):
        print("\n*********You entered wrong type**********")
        a=input("\nEnter again type(int or float) : ")
        return a
    else:
        return a

def type_cast(t,a):
    l=len(t)
    for i in range(l):
        if(t[i]=='0' or t[i]=='1' or t[i]=='2' or t[i]=='3' or t[i]=='4' or t[i]=='5' or
           t[i]=='6' or t[i]=='7' or t[i]=='8' or t[i]=='9' or t[i]=='.'):

            if(t[i]==t[l-1]):
                
                if(a=='int'):
                    t=int(t)
                    return t
                else:
                    t=float(t)
                    return t
                    

        else:
            print("You entered string in value , arith ope cannot be perform on strings ")
            exit()
        
        
#--------------------calculator----------------------------

cal='n'
while(cal=='n'):
    print("\n\n-----------------Calculator started--------------")
    ch=str.lower(input("Enter which type of value you want to enter(int or float) : "))
    y=0
    while(y==0):
        ch=check(ch)
        if(ch== 'int' or ch == 'float'):
            break


    print("\n---------------------------------------------------------------")
    op_type=input("For (square,cube,square root) operation enter '1' \nFor (+,-,*,/,%) operation enter 2 : ")
    print("---------------------------------------------------------------")

    if(op_type=='1'):
        u=input("\nEnter value : ")
        u=type_cast(u,ch)

        print("\nEnter s for square \n c for cube \n sr for square root")
        op=str.lower(input("\nEnter which operation you want to perform : "))

        if(op=='s'):
            i=square(u)
            print("\nAns :- Square of",u,":",i)

        elif(op=='c'):
            i=cube(u)
            print("\nAns :- Cube of",u,":",i)

        elif(op=='sr'):
            i=squ_root(u)
            print("\nAns :- Square root of",u,":",i)

        else:
            print("\n*******You entered wrong choice****")

        
        
    elif(op_type=='2'):
        a,b=input("\nEnter 1st value : "),input("Enter 2nd value : ")
        a=type_cast(a,ch)
        b=type_cast(b,ch)

        print("\nEnter + for adition \n - for subtraction \n * for Multiplication \n / for division \n % for modulo")

        op=input("\nEnter which operation you want to perform : ")

        if(op=='+'):
            i=add(a,b)
            print("\nAns : ",a,"+",b,"=",i)
    
        elif(op=='-'):
            i=subtract(a,b)
            print("\nAns : ",a,"-",b,"=",i)
    
        elif(op=='*'):
            i=multiply(a,b)
            print("\nAns : ",a,"*",b,"=",i)
    
        elif(op=='/'):
            if(b==0):
                print("\n*****Division by 0 is not allowed******")
            else:
                i=divide(a,b)
                print("\nAns : ",a,"/",b,"=",i)
        
        elif(op=='%'):
            if(b==0):
                print("\n*****Division by 0 is not allowed*****")
            else:
                i=modulo(a,b)
                print("\nAns : ",a,"%",b,"=",i)
    
    cal=input("\n--------->For use again enter 'n' or for exit enter anything : ")

    

