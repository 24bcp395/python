def len(string):
    if string=="":
        return 0
    else:
        return 1+len(string[1:])
    
string=input("enetr here:")

print(len(string))