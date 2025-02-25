names=set()

for i in range(5):
    a=input("enter a name here:")
    names.add(a)
    names.add("bhuva")
    
name1=input("enter you delet:")
name2=input("enetr you delet:")
names.discard(name1)
names.discard(name2)
print(names)

