# Sum of natural numbers up to num

num = int(input("Enter limit of sum : "))

sum = 0
   
for i in range(1,num+1):
    sum += num
    num -= 1
print("The sum is", sum)
