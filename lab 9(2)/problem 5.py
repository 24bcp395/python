def apowb(a,b):
    
    if b==0:
        return 1
    else:
        return a*apowb(a,b-1)
    
a=int(input("enter here a:"))
b=int(input("enter here b:"))

print(apowb(a,b))