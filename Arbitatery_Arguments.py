def avg(*value):
    x=0
    for i in value:
        x+=i    
    return x/len(value)
# Values is passing as Tuple
y = avg(1,2,3,4,5,6,7)
z = avg(2,3,4,4,2)
s = avg(6,5,4)

print(s,z,y)


