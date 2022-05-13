a=int(input("Enter a num : "))

print("Divisors of",a,"--->")
for i in range(2,a+1):
    if(a%i==0):
        print(i)


