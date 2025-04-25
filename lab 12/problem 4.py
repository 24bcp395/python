import math

class Regularshape:
    def __init__(self,num_sides=0,side_length=0):
        self.num_sides=num_sides
        self.side_length=side_length
        
    def perimeter(self):
        return self.num_sides*self.side_length
    
    def area(self):
        print("side is not less than 3")
        
        n=self.num_sides
        s=self.side_length
        return (n * s**2) / (4 * math.tan(math.pi /n))
    
    def getvalue(self):
        self.num_sides=int(input("enter sides number:"))
        self.side_length=int(input("enter length here:"))
        
a=Regularshape()
a.getvalue()    
print("your area is:",a.area())
print("your perimter is:",a.perimeter()) 
        