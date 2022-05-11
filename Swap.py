a=input("Enter a num : ")
b=input("Enter a num : ")

print("\n-----------Values before swapping--------")

print("\nFirst num : ",a,"\nSecond num : ",b)

temp=a
a=b
b=temp

print("\n-----------Values after swapping--------")

print("\nFirst num : "+a+"\nSecond num : "+b)

#Second method of swapping
a=int(input("Enter a num : "))
b=int(input("Enter a num : "))

print("\n-----------Values before swapping--------")

print("\nFirst num : ",a,"\nSecond num : ",b)

a=a+b
b=a-b
a=a-b

print("\nFirst num : "+a+"\nSecond num : "+b)

