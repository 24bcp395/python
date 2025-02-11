#lst1=[1,2,3,4,5]
#lst2=[2,5,1,7,8]
import random
lst1=[random.randint(1,30) for i in range(5)]
lst2=[random.randint(1,30) for i in range(5)]
print("lst1=",lst1)
print("lst2=",lst2)
lst3=[num for num in lst1 if num not in lst2]
print("new lst :",lst3)
