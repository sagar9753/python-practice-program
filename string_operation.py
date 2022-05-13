str1="I am fine"
length=len(str1)
print("length of string :: ",length)
print("length of string :: "+str(length))
print("length of string :: {} ".format(length))
print("------------------------------")
for i in range(length):
    print(str1[i]," is at index ",i)
print("------------------------------")

for i in str1:
    print(i,"is at index :: ",str1.index(i))
print("------------------------------")
for i in range(length-1,-1,-1):
    print(str1[i]," is at index ",i)
