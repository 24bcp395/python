n=int(input("enetr n number here:"))
r=int(input("enetr a r here:"))
substrac=n-r
factorial_n=1
for i in range(1,n+1):
    factorial_n=factorial_n*i
print("n!","=",factorial_n)

factorial_r=1
for i in range(1,r+1):
    factorial_r=factorial_r*i
print("r!","=",factorial_r)

factorial_nr=1
for i in range(1,(n-r)+1):
    factorial_nr=factorial_nr*i
print("(n-r)!","=",factorial_nr)

ncr=(factorial_n)/(factorial_r*factorial_nr)
print("ncr","=",ncr)
npr=factorial_n/factorial_nr
print("npr","=",npr)
    
    