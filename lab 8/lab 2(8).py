import random
rset={random.randint(15,45) for i in range(10)}
print(rset)
new_set=set()
count=0
for numbers in rset:
    if numbers<=35:
        new_set.add(numbers)
        count+=1
print(new_set)
print("numbers are less then 35 =",count)