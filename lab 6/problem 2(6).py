lst=[(1,"manav",19),(3,"ujash",19),(5,"prince",20)]
name=[]
roll=[]
age=[]
for element in lst:
    name.append(element[1])
    roll.append(element[0])
    age.append(element[2])
    
print(name)
print(roll)
print(age)