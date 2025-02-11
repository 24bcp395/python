string=input("enter a string here:")
result=""

if string=="lower":
    
    for i in range(len(string)):
        if 'a'<= string[i] <='z':
            result+=chr(ord(string[i])-32)
            
        else:
            result+=i


elif string=="upper":
    for i in range(len(string)):
        if 'A'<= string[i] <='Z':
            result+=chr(ord(string[i])+32)
            
        else:
            result+=i

else:
    for i in range(len(string)):
        if 'a'<= string[i] <='z':
            result+=chr(ord(string[i])-32)
        elif 'A'<= string[i] <='Z':
            result+=chr(ord(string[i])+32)
        
print(result)
            




