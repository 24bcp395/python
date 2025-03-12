def sum_avg():
    sum=0
    for i in range(1,6):
        a=int(input("enetr a marks here:"))
        sum+=a
    avg=sum/5
    dic={"total":sum,"avg":avg}
    return print(dic)
sum_avg()
