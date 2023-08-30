class Circle:
    def __init__(self,radius):
        self.radius = radius
    def Perimeter(self):
        r = self.radius
        perimeter = (2*(3.14)*r)
        print("Perimeter of the Cicle is ",perimeter,"cm")
    def Area(self):
        r = self.radius
        area = ((3.14)*(r**2))
        print("Area of Circle is ",area,"cm²")
class Rectangular:
    def __init__(self,length,breath):
        self.length = length
        self.breath = breath
    def Permeter(self):
        p = 2*(self.length+self.breath)
        print("Perimeter of the rectangular is",p,"cm")
    def Area(self):
        l = self.length
        b = self.breath
        area = (l*b)
        print("Area of the rectangular is ",area,"cm²")

shape = input("Enter the shape name Rectangular or Circle :")
find = input("Perimeter or Area :")

if shape=="Rectangular":
    r = Rectangular((int(input("Enter the length of the rectangular :"))),(int(input("Enter the breath of the rectangular :"))))
    if find=="Area":
        r.Area()
    if find=="Perimeter":
        r.Permeter()
    else:
        print("CHECK THE SPELLING")
if shape=="Circle":
    c = Circle((int(input("Enter the radius of the circle :"))))
    if find=="Area":
        c.Area()
    if find=="Perimeter":
        c.Perimeter()
    else:
        print("CHECK THE SPELLING")

else:
    print("INVALID SHAPE")





