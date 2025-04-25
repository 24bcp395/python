f1=open("C:\\Users\\Mac\\Documents\\python\\f1.txt","r")
f2=open("C:\\Users\\Mac\\Documents\\python\\f2.txt","r")
f=open("C:\\Users\\Mac\\Documents\\python\\f.txt","w")

linesf1=f1.readlines()
linesf2=f2.readlines()

f1.close()
f2.close()

max_len=max(len(linesf1),len(linesf2))

for i in range(max_len):
    if i<len(linesf1):
        f.write(linesf1[i])
    if i<len(linesf2):
        f.write(linesf2[i])

f.close()
print("file merged succesfully")