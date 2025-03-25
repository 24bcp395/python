def reverse(list):
    if list==[]:
        return []
    else:
        return reverse(list[1:])+[list[0]]
list=[]   
n=int(input("element number:"))
for i in range(n):
    element=input("enter here:")
    list.append(element)    
print(reverse(list))