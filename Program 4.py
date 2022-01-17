import math
class Triangle:
    def __init__(self,side1,side2,side3,S):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.S = S
    def  displayAttributes(self):
        print("side 1 is", self.side1,",", "side2 is", self.side2,",","side3 is",self.side3,",","value of S is",self.S)
    def getArea(self):
        return math.sqrt(S*((S-self.side1)*(S-self.side2)*(S-self.side3)))
    def parameter(self):
        return self.side1 + self.side2 + self.side3

side1 = int(input("enter side1: "))
side2 = int(input("enter side2: "))
side3 = int(input("enter side3: "))
S = (side1 + side2 + side3)/2
Triangle = Triangle(side1,side2,side3,S)
Triangle.displayAttributes()
print("Area of Triangle is", Triangle.getArea())
print("parameter of Triangle is", Triangle.parameter())