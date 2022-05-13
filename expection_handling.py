#try except finally 
def function():
	pass
try : 
	a = int(input("Enter a Value : "))
	b = int(input("Enter a Value : "))
	c = a/b 
	print("{}/{}={}".format(a,b,c))

except ZeroDivisionError :
	print("Number can not be divisible by zero")

except ValueError : 
	print("Please Provide a Integer value only")





