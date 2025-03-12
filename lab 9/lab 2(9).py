"""def compute():
    a=input("enter a number here:")
    n=int(a)
    nn=int(str(n)*2)
    nnn=int(str(n)*3)
    nnnn=int(str(n)*4)

    sum=n+nn+nnn+nnnn
    print(sum)
compute()
"""

def compute():
    a=input("enter a number here:")
    total=0
    for i in range(1,5):
        num=int(str(a)*i)
        total+=num
        print(num)
    print(total)
        
compute()