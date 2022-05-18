
class calculation():
    def area(self,para1=None,para2=None):
        if (para1 != None and para2!= None ):     # Area of Rectangle
            area  = para1 * para2
            return area
        elif (para1 != None and para2 == None):  # Area of Circle
            area= 3.14 * para1 *para1
            return area
        else :  # Nothing is Passed 
            area = "No Parameter passed "
            return area
x = calculation()
rectangle = x.area(12,3)
circle =  x.area(12)
circle= round(circle , 2 )
Nothing = x.area()

print("Area of Rectangle : ",rectangle)
print("Area of Rectangle : ",circle)
print("Area of Nothing : ",Nothing)




            





