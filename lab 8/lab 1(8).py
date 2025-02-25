lst=["manav","ujash","prince"]
upper=[]

for string in lst:
    upercase=""
    for char in string:
        if "a"<=char<="z":
            upercase+=chr(ord(char)-32)
        else:
            upercase+=1
    upper.append(upercase) 
            
print(upper)

set=set(upper)
print(set)