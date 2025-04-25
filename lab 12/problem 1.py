class Complex:
    def __init__(self,r=0,i=0):
        self.r=r
        self.i=i
        
    def __str__(self):
        if self.i<0:
            op=""
        else:
            op="+"
        return f"{self.r}{op}{self.i}i"
    
    def getvalue(self):
        print("enter complex value one by one:")
        self.r=float(input())
        self.i=float(input())
        
    def __add__(self,other):
        ans=Complex()
        ans.r=self.r+other.r
        ans.i=self.i+other.i
        return ans
    
    def __sub__(self,other):
        anssub=Complex()
        anssub.r=self.r-other.r
        anssub.i=self.i-other.i
        return anssub
    
    def __mul__(self,other):
        ansmul=Complex()
        ansmul.r=self.r*other.r-self.i*other.i
        return ansmul
    
    def __truediv__(self, other):
        denominator = other.r**2 + other.i**2
    
        real= (self.r * other.r + self.i * other.i) / denominator
        image= (self.i * other.r - self.r * other.i) / denominator
        return Complex(real,image)
    
a=Complex()
a.getvalue()
print(a)
b=Complex()
b.getvalue()
print(b)
c=a+b
print("your addition:",c)
d=a-b
print("ypour substraction:",d)
e=a*b
print("your multiplication:",e)
f=a/b
print("your division:",f)