import math
a=int(input("enter a number here:"))
def is_prime(a):
    
    if a<=1:
        print("a number is not prime")
        
    for i in range(2,int(math.sqrt(a)+1)):
        if a%i==0:
            print(a,"not a prime number")
        return
            
print("number is prime")
            

def palindrom(a):
    reversenumber=0
    originalnumber=a
    
    while a!=0:
        remainder=a%10
        reversenumber=(reversenumber*10)+remainder
        a=a//10   #integer division
        
    if originalnumber==reversenumber:
        print(originalnumber,"number is palindrome")
    else:
        print(originalnumber,"is not palindrome")
        
     
def armstrong(a):
    sum=0
    digits=str(a)
    pow=len(digits)
    for digit in digits:
        sum+=int(digit)**pow
        
    if sum==a:
        print(a,"number is armstrong")
    else:
        print("not armstrong")
        


def perfect(a):
    sum=0
    
    for i in range(1,a):
        if a%i==0:
            sum+=i
        
    if sum==a:
         print(a,"perfect") 
    else:
        print("not perfect")
        
def automorphic():
    num=int(input("enetr here:"))
    square=num*num
    
    temp=num
    pow10=1
    
    while temp>0:
        pow10*=10
        temp//=10
        
        
    if square%pow10==num:
        print(num,"is automorphic")
    else:
        print(num,"is not automorphic")
        

is_prime(a)
palindrom(a)
armstrong(a)
perfect(a)
automorphic()