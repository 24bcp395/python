import random
odd=random.sample(range(1,100,2),5)
print("odd :",odd)
even=random.sample(range(2,100,2),5)
print("even :",even)
odd[2]=even
print(odd)
empty=[]
for item in odd:
    if isinstance(item,list):
        empty.extend(item)
    else:
        empty.append(item)
print("empty :",empty)