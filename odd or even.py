num=input("Enter a number : ")
num=float(num)
print(type(num))

x=num%2
print(x)

if(num==0):
    print("Number is neither even nor odd")
elif(num%2==0):
    print("Number is even")
else:
    print("Number is odd")


