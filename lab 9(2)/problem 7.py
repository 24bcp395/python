def avg(lst,index=0,sum=0):
    if index==len(lst):
        return sum/len(lst)
    

    sum+=lst[index]
    return avg(lst,index+1,sum)
    
lst=[1,2,3,3,4,5]
    
print(avg(lst))