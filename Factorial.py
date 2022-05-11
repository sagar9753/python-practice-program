def fact(n):
    fact=1
    if(n==0):
        return 1
    else:
        for i in range(1,n+1):
            fact=fact*i
        return fact


a=int(input("Enter a num : "))
n=fact(a)
print("Factorial of",a,"is :",n)
