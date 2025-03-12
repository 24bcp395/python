def crtlst(n):
    lst=[]
    n=int(input("enter a last number here:"))
    for i in range(1,n+1):
        s=i,i**2,i**3
        tpl=tuple(s)
        lst.append(tpl)
        print(lst)
        
crtlst(n)        
