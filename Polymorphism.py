def Area(self,Length,Width):
    self.Length = Length
    self.Width = Width
    return Length*Width
def Area(self,radius):
    self.radius = radius
    return 3.14 *self.radius*self.radius

length = 4
width = 5
radius = 3

print("Area Of Rectangle :",Area(length,width))
print("Area Of Circle :",Area(radius))