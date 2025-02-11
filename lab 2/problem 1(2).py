def large():
    a=int(input("enter a number here:"))
    b=int(input("enter b number here:"))
    c=int(input("enter c number here:"))

    if(a>=b and a>=c):
        print("largest",a)
    elif(b>=c):
        print("largest",b)
    else:
        print("largest",c)

    if(a<=b and a<=c):
        print("smalest",a)
    elif(b<=c):
        print("smalest",b)
    else:
        print("smalest",c)

large()
        
   



