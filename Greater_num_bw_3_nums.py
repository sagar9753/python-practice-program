a=int(input("Enter the first number : "))
b=int(input("Enter the secont number : "))
c=int(input("Enter the third number : "))

if(a==b==c):
    print("All values are same")
elif(a==b):
    if(c>a or c>b):
        print("a and b are equal and c is greater")
    else:
        print("a and b are equal and c is lesser")
elif(a==c):
    if(b>a or b>c):
        print("a and b are equal and c is greater")
    else:
        print("a and b are equal and c is lesser")
elif(b==c ):
    if(a>b or a>c):
        print("a and b are equal and c is greater")
    else:
        print("a and b are equal and c is lesser")
elif(a>b and a>c):
    print(a,"is greater than",b,"and",c)
elif(b>a and b>c):
    print(b,"is greater than",a,"and",c)
else:
    print(c,"is greater than",a,"and",b)
