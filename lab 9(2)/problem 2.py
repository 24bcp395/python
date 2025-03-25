def binary(a):
    if a==0:
        return ""
    
    return binary(a//2)+str(a%2)

a=int(input("enter number here:"))
if a>0:
    print(binary(a))
else:
    print("enter a positive number")