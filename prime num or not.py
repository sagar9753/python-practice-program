a=int(input("Enter a num : "))


for i in range(2,a-1):
    if(a%i==0):
        print("Prime not")
        break
        
else:
    print("The num is prime")
