a=int(input("Enter a num : "))

#n=10
#for i in range(1,n+1,1):
#    print(a,"*",i,"=",a*i)

n=a*10
count=1
for i in range(a,n+1,a):
    print("{}*{}={}".format(n,count,i))
    count=count+1
