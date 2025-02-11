def triangle():
    a=float(input("enter first angle here:"))
    b=float(input("enter second angle here:"))
    c=float(input("enter third angle here:"))
    sum=a+b+c
    
    if(sum==180):
        print("triagle is valid")
    else:
        print("triangle is not valid")

triangle()
