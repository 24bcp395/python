import operator
lst=[("panipuri",100),("pizza",500),("puff",50)]
for i in range(len(lst)):
    sorted(lst,key=operator.itemgetter(1))

print(sorted(lst,key=operator.itemgetter(1)))
