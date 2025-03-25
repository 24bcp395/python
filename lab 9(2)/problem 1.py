def factors(number,divisior=2):
    if number==1:
        return []
    
    if number%divisior==0:
        return [divisior]+factors(number//divisior,divisior) #this is reduce the number number//divisior
    else:
        return factors(number,divisior+1)
    
number=int(input("enetr here:"))
if number>0:
    print("factors is :",factors(number))
else:
    print("enter positive number here")