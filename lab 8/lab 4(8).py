new=set()
for i in range(5):
    a=input("enter names here:")
    new.add(a)
print(new)

A=set()
B=set()
for name in new:
    for char in name:
        if name[0]=="A":
            A.add(name)
        elif name[-1]=="B":
            B.add(name)
            
        
            
print("name START with a:",A)
print("name END with b:",B)