#    ------------ For Circle Class -------------------



class circle:
     def __init__ (self,radius):
         self.radius = radius
    
     def area(self,radius):
         return 3.14*self.radius*self.radius
     def circum(self,radius):
         return 2*3.14*self.radius

radius = int(input("Enter Radius of Circle : "))
cir1= circle(radius)
print("Area : ",cir1.area(radius))
print("Circum : ",cir1.circum(radius))


